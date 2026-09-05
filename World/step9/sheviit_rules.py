#!/usr/bin/env python3
# sheviit_rules.py — round 47, THE TOPIC-ROUTED DOCKET SUPPLEMENT
# (2026-09-05, after compaction #51; REVIEW_BEHAR item 2). Mishnah
# Sheviit whole + the unread rows of Arakhin, Temurah, Bekhorot 9, and
# Bava Metzia 5, routed BY TOPIC. GENERATED from the same table as
# cases_sheviit.yaml and the vocabulary (scratchpad/gen_sheviit_cases.py)
# — the three artifacts cannot drift. Read-source:
# logic/oral_triage/sheviit_topic_docket_2026-09-05.md. Eight modules,
# 189 cells over 131 LAW rows; every dispute returned whole with its arms
# labeled; the release module answers talmud_source-only (routed).

TABLE = {'sheviit_labor_file': {'tractate': 'Sheviit',
                        'oracle': 'Mishnah Sheviit 1:1; 1:2; 1:3; 1:5; 1:6; 1:7; 1:8; 2:1; 2:2; '
                                  '2:3; 2:4; 2:5; 2:6; 2:7; 2:8; 2:9; 2:10; 3:1; 3:2; 3:3; 3:4; '
                                  '3:5; 3:6; 3:7; 3:8; 3:9; 3:10; 4:1; 4:2; 4:3; 4:4; 4:5; 4:6; '
                                  '4:10; Babylonian Talmud Moed Katan 3a:1; 3a:9; 3a:11; 3a:12; '
                                  '3b:8; 3b:12; 4a:9',
                        'claim': 'LV25A-04',
                        'anchor': 'Lev.25.1-7 (lev_25_shemittah, LV25A-02, LV25A-03, LV25A-04, '
                                  'LV25A-19)',
                        'cells': {'sheviit_orchard_plow_cutoff_eve': [('beit_shammai_while_it_benefits',
                                                                       'Beit Shammai',
                                                                       'Mishnah Sheviit 1:1 — '
                                                                       'until when do they plow an '
                                                                       'orchard on the eve; seat: '
                                                                       'the labor census and the '
                                                                       'class rule (LV25A-04), the '
                                                                       'thirty-day addition on the '
                                                                       'onset timeline (LV25A-02), '
                                                                       'the rooting rule '
                                                                       "(LV25A-03); the Talmud's "
                                                                       'LAYER label seated this '
                                                                       'sitting (LV25A-19)'),
                                                                      ('beit_hillel_until_atzeret',
                                                                       'Beit Hillel',
                                                                       'Mishnah Sheviit 1:1 — '
                                                                       'until when do they plow an '
                                                                       'orchard on the eve; seat: '
                                                                       'the labor census and the '
                                                                       'class rule (LV25A-04), the '
                                                                       'thirty-day addition on the '
                                                                       'onset timeline (LV25A-02), '
                                                                       'the rooting rule '
                                                                       "(LV25A-03); the Talmud's "
                                                                       'LAYER label seated this '
                                                                       'sitting (LV25A-19)')],
                                  'sheviit_orchard_definition': [('three_trees_sixty_maneh_cake',
                                                                  None,
                                                                  'Mishnah Sheviit 1:2 — three '
                                                                  'trees to the standard plot; '
                                                                  'seat: the labor census and the '
                                                                  'class rule (LV25A-04), the '
                                                                  'thirty-day addition on the '
                                                                  'onset timeline (LV25A-02), the '
                                                                  'rooting rule (LV25A-03); the '
                                                                  "Talmud's LAYER label seated "
                                                                  'this sitting (LV25A-19)')],
                                  'sheviit_barren_tree_threshold': [('viewed_as_figs',
                                                                     None,
                                                                     'Mishnah Sheviit 1:3 — they '
                                                                     'are viewed as if they were '
                                                                     'figs; seat: the labor census '
                                                                     'and the class rule '
                                                                     '(LV25A-04), the thirty-day '
                                                                     'addition on the onset '
                                                                     'timeline (LV25A-02), the '
                                                                     'rooting rule (LV25A-03); the '
                                                                     "Talmud's LAYER label seated "
                                                                     'this sitting (LV25A-19)')],
                                  'sheviit_three_trees_three_owners': [('combine_ox_with_gear_spacing',
                                                                        None,
                                                                        'Mishnah Sheviit 1:5 — so '
                                                                        'that the ox passes with '
                                                                        'its gear; seat: the labor '
                                                                        'census and the class rule '
                                                                        '(LV25A-04), the '
                                                                        'thirty-day addition on '
                                                                        'the onset timeline '
                                                                        '(LV25A-02), the rooting '
                                                                        'rule (LV25A-03); the '
                                                                        "Talmud's LAYER label "
                                                                        'seated this sitting '
                                                                        '(LV25A-19)')],
                                  'sheviit_ten_saplings_scattered': [('plow_whole_plot_until_new_year',
                                                                      None,
                                                                      'Mishnah Sheviit 1:6 — ten '
                                                                      'saplings scattered; seat: '
                                                                      'the labor census and the '
                                                                      'class rule (LV25A-04), the '
                                                                      'thirty-day addition on the '
                                                                      'onset timeline (LV25A-02), '
                                                                      'the rooting rule '
                                                                      "(LV25A-03); the Talmud's "
                                                                      'LAYER label seated this '
                                                                      'sitting (LV25A-19)')],
                                  'sheviit_saplings_and_gourds': [('combine',
                                                                   None,
                                                                   'Mishnah Sheviit 1:7 — the '
                                                                   'saplings and the gourds '
                                                                   'combine; seat: the labor '
                                                                   'census and the class rule '
                                                                   '(LV25A-04), the thirty-day '
                                                                   'addition on the onset timeline '
                                                                   '(LV25A-02), the rooting rule '
                                                                   "(LV25A-03); the Talmud's LAYER "
                                                                   'label seated this sitting '
                                                                   '(LV25A-19)')],
                                  'sheviit_when_sapling_becomes_tree': [('r_elazar_b_azaryah_until_profane',
                                                                         'R. Elazar b. Azaryah',
                                                                         'Mishnah Sheviit 1:8 — '
                                                                         'until when are they '
                                                                         'called saplings; seat: '
                                                                         'the labor census and the '
                                                                         'class rule (LV25A-04), '
                                                                         'the thirty-day addition '
                                                                         'on the onset timeline '
                                                                         '(LV25A-02), the rooting '
                                                                         'rule (LV25A-03); the '
                                                                         "Talmud's LAYER label "
                                                                         'seated this sitting '
                                                                         '(LV25A-19)'),
                                                                        ('r_yehoshua_seven_years',
                                                                         'R. Yehoshua',
                                                                         'Mishnah Sheviit 1:8 — '
                                                                         'until when are they '
                                                                         'called saplings; seat: '
                                                                         'the labor census and the '
                                                                         'class rule (LV25A-04), '
                                                                         'the thirty-day addition '
                                                                         'on the onset timeline '
                                                                         '(LV25A-02), the rooting '
                                                                         'rule (LV25A-03); the '
                                                                         "Talmud's LAYER label "
                                                                         'seated this sitting '
                                                                         '(LV25A-19)'),
                                                                        ('r_akiva_as_its_name',
                                                                         'R. Akiva',
                                                                         'Mishnah Sheviit 1:8 — '
                                                                         'until when are they '
                                                                         'called saplings; seat: '
                                                                         'the labor census and the '
                                                                         'class rule (LV25A-04), '
                                                                         'the thirty-day addition '
                                                                         'on the onset timeline '
                                                                         '(LV25A-02), the rooting '
                                                                         'rule (LV25A-03); the '
                                                                         "Talmud's LAYER label "
                                                                         'seated this sitting '
                                                                         '(LV25A-19)')],
                                  'sheviit_grain_field_plow_cutoff_eve': [('until_moisture_ends',
                                                                           None,
                                                                           'Mishnah Sheviit 2:1 — '
                                                                           'until the moisture '
                                                                           'ends; seat: the labor '
                                                                           'census and the class '
                                                                           'rule (LV25A-04), the '
                                                                           'thirty-day addition on '
                                                                           'the onset timeline '
                                                                           '(LV25A-02), the '
                                                                           'rooting rule '
                                                                           '(LV25A-03); the '
                                                                           "Talmud's LAYER label "
                                                                           'seated this sitting '
                                                                           '(LV25A-19)')],
                                  'sheviit_r_shimon_fixed_cutoffs': [('grain_passover_orchard_atzeret',
                                                                      None,
                                                                      'Mishnah Sheviit 2:1 — in '
                                                                      'the grain field until '
                                                                      'Passover; seat: the labor '
                                                                      'census and the class rule '
                                                                      '(LV25A-04), the thirty-day '
                                                                      'addition on the onset '
                                                                      'timeline (LV25A-02), the '
                                                                      'rooting rule (LV25A-03); '
                                                                      "the Talmud's LAYER label "
                                                                      'seated this sitting '
                                                                      '(LV25A-19)')],
                                  'sheviit_fertilize_hoe_beds_eve': [('until_new_year',
                                                                      None,
                                                                      'Mishnah Sheviit 2:2 — they '
                                                                      'fertilize and hoe until the '
                                                                      'New Year; seat: the labor '
                                                                      'census and the class rule '
                                                                      '(LV25A-04), the thirty-day '
                                                                      'addition on the onset '
                                                                      'timeline (LV25A-02), the '
                                                                      'rooting rule (LV25A-03); '
                                                                      "the Talmud's LAYER label "
                                                                      'seated this sitting '
                                                                      '(LV25A-19)')],
                                  'sheviit_remove_leaf_from_cluster_in_seventh': [('r_shimon_permits',
                                                                                   None,
                                                                                   'Mishnah '
                                                                                   'Sheviit 2:2 — '
                                                                                   'he even '
                                                                                   'removes the '
                                                                                   'leaf; seat: '
                                                                                   'the labor '
                                                                                   'census and the '
                                                                                   'class rule '
                                                                                   '(LV25A-04), '
                                                                                   'the thirty-day '
                                                                                   'addition on '
                                                                                   'the onset '
                                                                                   'timeline '
                                                                                   '(LV25A-02), '
                                                                                   'the rooting '
                                                                                   'rule '
                                                                                   '(LV25A-03); '
                                                                                   "the Talmud's "
                                                                                   'LAYER label '
                                                                                   'seated this '
                                                                                   'sitting '
                                                                                   '(LV25A-19)')],
                                  'sheviit_trim_prune_shoots_eve': [('until_new_year',
                                                                     None,
                                                                     'Mishnah Sheviit 2:3 — '
                                                                     'trimming, pruning shoots, '
                                                                     'cutting dead wood; seat: the '
                                                                     'labor census and the class '
                                                                     'rule (LV25A-04), the '
                                                                     'thirty-day addition on the '
                                                                     'onset timeline (LV25A-02), '
                                                                     'the rooting rule (LV25A-03); '
                                                                     "the Talmud's LAYER label "
                                                                     'seated this sitting '
                                                                     '(LV25A-19)')],
                                  'sheviit_water_saplings_eve': [('until_new_year',
                                                                  None,
                                                                  'Mishnah Sheviit 2:4 — and water '
                                                                  'them until the New Year; seat: '
                                                                  'the labor census and the class '
                                                                  'rule (LV25A-04), the thirty-day '
                                                                  'addition on the onset timeline '
                                                                  '(LV25A-02), the rooting rule '
                                                                  "(LV25A-03); the Talmud's LAYER "
                                                                  'label seated this sitting '
                                                                  '(LV25A-19)')],
                                  'sheviit_water_foliage_in_seventh': [('r_elazar_b_tzadok_foliage_not_root',
                                                                        None,
                                                                        'Mishnah Sheviit 2:4 — he '
                                                                        'waters the foliage; seat: '
                                                                        'the labor census and the '
                                                                        'class rule (LV25A-04), '
                                                                        'the thirty-day addition '
                                                                        'on the onset timeline '
                                                                        '(LV25A-02), the rooting '
                                                                        'rule (LV25A-03); the '
                                                                        "Talmud's LAYER label "
                                                                        'seated this sitting '
                                                                        '(LV25A-19)')],
                                  'sheviit_oil_unripe_figs_crossing_year': [('not_oiled',
                                                                             None,
                                                                             'Mishnah Sheviit 2:5 '
                                                                             '— not oiled and not '
                                                                             'pierced; seat: the '
                                                                             'labor census and the '
                                                                             'class rule '
                                                                             '(LV25A-04), the '
                                                                             'thirty-day addition '
                                                                             'on the onset '
                                                                             'timeline (LV25A-02), '
                                                                             'the rooting rule '
                                                                             '(LV25A-03); the '
                                                                             "Talmud's LAYER label "
                                                                             'seated this sitting '
                                                                             '(LV25A-19)')],
                                  'sheviit_plant_sink_graft_before_new_year': [('thirty_days_else_uproot',
                                                                                None,
                                                                                'Mishnah Sheviit '
                                                                                '2:6 — less than '
                                                                                'thirty days; '
                                                                                'seat: the labor '
                                                                                'census and the '
                                                                                'class rule '
                                                                                '(LV25A-04), the '
                                                                                'thirty-day '
                                                                                'addition on the '
                                                                                'onset timeline '
                                                                                '(LV25A-02), the '
                                                                                'rooting rule '
                                                                                '(LV25A-03); the '
                                                                                "Talmud's LAYER "
                                                                                'label seated this '
                                                                                'sitting '
                                                                                '(LV25A-19)')],
                                  'sheviit_graft_taking_time': [('r_yehuda_three_days',
                                                                 'R. Yehuda',
                                                                 'Mishnah Sheviit 2:6 — any graft '
                                                                 'that does not take; seat: the '
                                                                 'labor census and the class rule '
                                                                 '(LV25A-04), the thirty-day '
                                                                 'addition on the onset timeline '
                                                                 '(LV25A-02), the rooting rule '
                                                                 "(LV25A-03); the Talmud's LAYER "
                                                                 'label seated this sitting '
                                                                 '(LV25A-19)'),
                                                                ('r_yosei_r_shimon_two_weeks',
                                                                 'R. Yosei and R. Shimon',
                                                                 'Mishnah Sheviit 2:6 — any graft '
                                                                 'that does not take; seat: the '
                                                                 'labor census and the class rule '
                                                                 '(LV25A-04), the thirty-day '
                                                                 'addition on the onset timeline '
                                                                 '(LV25A-02), the rooting rule '
                                                                 "(LV25A-03); the Talmud's LAYER "
                                                                 'label seated this sitting '
                                                                 '(LV25A-19)')],
                                  'sheviit_rice_millet_rooted_before_new_year': [('past_year_permitted_in_seventh',
                                                                                  None,
                                                                                  'Mishnah Sheviit '
                                                                                  '2:7 — that '
                                                                                  'rooted before '
                                                                                  'the New Year; '
                                                                                  'seat: the labor '
                                                                                  'census and the '
                                                                                  'class rule '
                                                                                  '(LV25A-04), the '
                                                                                  'thirty-day '
                                                                                  'addition on the '
                                                                                  'onset timeline '
                                                                                  '(LV25A-02), the '
                                                                                  'rooting rule '
                                                                                  '(LV25A-03); the '
                                                                                  "Talmud's LAYER "
                                                                                  'label seated '
                                                                                  'this sitting '
                                                                                  '(LV25A-19)')],
                                  'sheviit_egyptian_bean_sown_for_seed': [('like_rooted_rule',
                                                                           None,
                                                                           'Mishnah Sheviit 2:8 — '
                                                                           'the Egyptian bean sown '
                                                                           'for seed; seat: the '
                                                                           'labor census and the '
                                                                           'class rule (LV25A-04), '
                                                                           'the thirty-day '
                                                                           'addition on the onset '
                                                                           'timeline (LV25A-02), '
                                                                           'the rooting rule '
                                                                           '(LV25A-03); the '
                                                                           "Talmud's LAYER label "
                                                                           'seated this sitting '
                                                                           '(LV25A-19)')],
                                  'sheviit_seedless_onions_water_withheld': [('thirty_days_past_year',
                                                                              None,
                                                                              'Mishnah Sheviit 2:9 '
                                                                              '— denied water '
                                                                              'thirty days; seat: '
                                                                              'the labor census '
                                                                              'and the class rule '
                                                                              '(LV25A-04), the '
                                                                              'thirty-day addition '
                                                                              'on the onset '
                                                                              'timeline '
                                                                              '(LV25A-02), the '
                                                                              'rooting rule '
                                                                              '(LV25A-03); the '
                                                                              "Talmud's LAYER "
                                                                              'label seated this '
                                                                              'sitting '
                                                                              '(LV25A-19)')],
                                  'sheviit_rainfed_water_withheld_seasons': [('r_meir_two',
                                                                              'R. Meir',
                                                                              'Mishnah Sheviit 2:9 '
                                                                              '— denied water two '
                                                                              'seasons; seat: the '
                                                                              'labor census and '
                                                                              'the class rule '
                                                                              '(LV25A-04), the '
                                                                              'thirty-day addition '
                                                                              'on the onset '
                                                                              'timeline '
                                                                              '(LV25A-02), the '
                                                                              'rooting rule '
                                                                              '(LV25A-03); the '
                                                                              "Talmud's LAYER "
                                                                              'label seated this '
                                                                              'sitting (LV25A-19)'),
                                                                             ('sages_three',
                                                                              'the Sages',
                                                                              'Mishnah Sheviit 2:9 '
                                                                              '— denied water two '
                                                                              'seasons; seat: the '
                                                                              'labor census and '
                                                                              'the class rule '
                                                                              '(LV25A-04), the '
                                                                              'thirty-day addition '
                                                                              'on the onset '
                                                                              'timeline '
                                                                              '(LV25A-02), the '
                                                                              'rooting rule '
                                                                              '(LV25A-03); the '
                                                                              "Talmud's LAYER "
                                                                              'label seated this '
                                                                              'sitting '
                                                                              '(LV25A-19)')],
                                  'sheviit_gourds_kept_for_seed_hardened': [('permitted_to_keep',
                                                                             None,
                                                                             'Mishnah Sheviit 2:10 '
                                                                             '— if they hardened '
                                                                             'before the New Year; '
                                                                             'seat: the labor '
                                                                             'census and the class '
                                                                             'rule (LV25A-04), the '
                                                                             'thirty-day addition '
                                                                             'on the onset '
                                                                             'timeline (LV25A-02), '
                                                                             'the rooting rule '
                                                                             '(LV25A-03); the '
                                                                             "Talmud's LAYER label "
                                                                             'seated this sitting '
                                                                             '(LV25A-19)')],
                                  'sheviit_dung_carried_to_heaps_when': [('r_meir_workers_cease',
                                                                          'R. Meir',
                                                                          'Mishnah Sheviit 3:1 — '
                                                                          'from when do they carry '
                                                                          'out dung; seat: the '
                                                                          'labor census and the '
                                                                          'class rule (LV25A-04), '
                                                                          'the thirty-day addition '
                                                                          'on the onset timeline '
                                                                          '(LV25A-02), the rooting '
                                                                          'rule (LV25A-03); the '
                                                                          "Talmud's LAYER label "
                                                                          'seated this sitting '
                                                                          '(LV25A-19)'),
                                                                         ('r_yehuda_sweet_dries',
                                                                          'R. Yehuda',
                                                                          'Mishnah Sheviit 3:1 — '
                                                                          'from when do they carry '
                                                                          'out dung; seat: the '
                                                                          'labor census and the '
                                                                          'class rule (LV25A-04), '
                                                                          'the thirty-day addition '
                                                                          'on the onset timeline '
                                                                          '(LV25A-02), the rooting '
                                                                          'rule (LV25A-03); the '
                                                                          "Talmud's LAYER label "
                                                                          'seated this sitting '
                                                                          '(LV25A-19)'),
                                                                         ('r_yosei_knots',
                                                                          'R. Yosei',
                                                                          'Mishnah Sheviit 3:1 — '
                                                                          'from when do they carry '
                                                                          'out dung; seat: the '
                                                                          'labor census and the '
                                                                          'class rule (LV25A-04), '
                                                                          'the thirty-day addition '
                                                                          'on the onset timeline '
                                                                          '(LV25A-02), the rooting '
                                                                          'rule (LV25A-03); the '
                                                                          "Talmud's LAYER label "
                                                                          'seated this sitting '
                                                                          '(LV25A-19)')],
                                  'sheviit_dung_heaps_measure': [('three_heaps_ten_baskets_letekh',
                                                                  None,
                                                                  'Mishnah Sheviit 3:2 — three '
                                                                  'heaps to the standard plot; '
                                                                  'seat: the labor census and the '
                                                                  'class rule (LV25A-04), the '
                                                                  'thirty-day addition on the '
                                                                  'onset timeline (LV25A-02), the '
                                                                  'rooting rule (LV25A-03); the '
                                                                  "Talmud's LAYER label seated "
                                                                  'this sitting (LV25A-19)')],
                                  'sheviit_more_than_three_heaps': [('r_shimon_permitted',
                                                                     'R. Shimon',
                                                                     'Mishnah Sheviit 3:3 — more '
                                                                     'than this — quarrying; seat: '
                                                                     'the labor census and the '
                                                                     'class rule (LV25A-04), the '
                                                                     'thirty-day addition on the '
                                                                     'onset timeline (LV25A-02), '
                                                                     'the rooting rule (LV25A-03); '
                                                                     "the Talmud's LAYER label "
                                                                     'seated this sitting '
                                                                     '(LV25A-19)'),
                                                                    ('sages_dig_or_raise_three',
                                                                     'the Sages',
                                                                     'Mishnah Sheviit 3:3 — more '
                                                                     'than this — quarrying; seat: '
                                                                     'the labor census and the '
                                                                     'class rule (LV25A-04), the '
                                                                     'thirty-day addition on the '
                                                                     'onset timeline (LV25A-02), '
                                                                     'the rooting rule (LV25A-03); '
                                                                     "the Talmud's LAYER label "
                                                                     'seated this sitting '
                                                                     '(LV25A-19)')],
                                  'sheviit_penning_cattle_fold': [('two_seah_fold_move_sides',
                                                                   None,
                                                                   'Mishnah Sheviit 3:4 — he makes '
                                                                   'a fold of two seahs; seat: the '
                                                                   'labor census and the class '
                                                                   'rule (LV25A-04), the '
                                                                   'thirty-day addition on the '
                                                                   'onset timeline (LV25A-02), the '
                                                                   'rooting rule (LV25A-03); the '
                                                                   "Talmud's LAYER label seated "
                                                                   'this sitting (LV25A-19)')],
                                  'sheviit_new_quarry_threshold': [('twenty_seven_stones',
                                                                    None,
                                                                    'Mishnah Sheviit 3:5 — their '
                                                                    'measure twenty-seven stones; '
                                                                    'seat: the labor census and '
                                                                    'the class rule (LV25A-04), '
                                                                    'the thirty-day addition on '
                                                                    'the onset timeline '
                                                                    '(LV25A-02), the rooting rule '
                                                                    "(LV25A-03); the Talmud's "
                                                                    'LAYER label seated this '
                                                                    'sitting (LV25A-19)')],
                                  'sheviit_fence_ten_two_man_stones': [('may_be_removed',
                                                                        None,
                                                                        'Mishnah Sheviit 3:6 — ten '
                                                                        'stones of two-man loads; '
                                                                        'seat: the labor census '
                                                                        'and the class rule '
                                                                        '(LV25A-04), the '
                                                                        'thirty-day addition on '
                                                                        'the onset timeline '
                                                                        '(LV25A-02), the rooting '
                                                                        'rule (LV25A-03); the '
                                                                        "Talmud's LAYER label "
                                                                        'seated this sitting '
                                                                        '(LV25A-19)')],
                                  'sheviit_stones_turned_by_plow': [('top_taken_ground_touching_left',
                                                                     None,
                                                                     'Mishnah Sheviit 3:7 — he '
                                                                     'takes the top ones; seat: '
                                                                     'the labor census and the '
                                                                     'class rule (LV25A-04), the '
                                                                     'thirty-day addition on the '
                                                                     'onset timeline (LV25A-02), '
                                                                     'the rooting rule (LV25A-03); '
                                                                     "the Talmud's LAYER label "
                                                                     'seated this sitting '
                                                                     '(LV25A-19)')],
                                  'sheviit_steps_at_ravines_eve_after_rains': [('forbidden_readies_for_seventh',
                                                                                None,
                                                                                'Mishnah Sheviit '
                                                                                '3:8 — no steps '
                                                                                'are built; seat: '
                                                                                'the labor census '
                                                                                'and the class '
                                                                                'rule (LV25A-04), '
                                                                                'the thirty-day '
                                                                                'addition on the '
                                                                                'onset timeline '
                                                                                '(LV25A-02), the '
                                                                                'rooting rule '
                                                                                '(LV25A-03); the '
                                                                                "Talmud's LAYER "
                                                                                'label seated this '
                                                                                'sitting '
                                                                                '(LV25A-19)')],
                                  'sheviit_shoulder_stones': [('r_meir_not_one_hand',
                                                               'R. Meir',
                                                               'Mishnah Sheviit 3:9 — shoulder '
                                                               'stones; seat: the labor census and '
                                                               'the class rule (LV25A-04), the '
                                                               'thirty-day addition on the onset '
                                                               'timeline (LV25A-02), the rooting '
                                                               "rule (LV25A-03); the Talmud's "
                                                               'LAYER label seated this sitting '
                                                               '(LV25A-19)'),
                                                              ('r_yosei_two_three_on_shoulder',
                                                               'R. Yosei',
                                                               'Mishnah Sheviit 3:9 — shoulder '
                                                               'stones; seat: the labor census and '
                                                               'the class rule (LV25A-04), the '
                                                               'thirty-day addition on the onset '
                                                               'timeline (LV25A-02), the rooting '
                                                               "rule (LV25A-03); the Talmud's "
                                                               'LAYER label seated this sitting '
                                                               '(LV25A-19)')],
                                  'sheviit_fence_earth_public_domain': [('r_yehoshua_heap_and_fix',
                                                                         'R. Yehoshua',
                                                                         'Mishnah Sheviit 3:10 — '
                                                                         'what does he do with the '
                                                                         'earth; seat: the labor '
                                                                         'census and the class '
                                                                         'rule (LV25A-04), the '
                                                                         'thirty-day addition on '
                                                                         'the onset timeline '
                                                                         '(LV25A-02), the rooting '
                                                                         'rule (LV25A-03); the '
                                                                         "Talmud's LAYER label "
                                                                         'seated this sitting '
                                                                         '(LV25A-19)'),
                                                                        ('r_akiva_into_his_field',
                                                                         'R. Akiva',
                                                                         'Mishnah Sheviit 3:10 — '
                                                                         'what does he do with the '
                                                                         'earth; seat: the labor '
                                                                         'census and the class '
                                                                         'rule (LV25A-04), the '
                                                                         'thirty-day addition on '
                                                                         'the onset timeline '
                                                                         '(LV25A-02), the rooting '
                                                                         'rule (LV25A-03); the '
                                                                         "Talmud's LAYER label "
                                                                         'seated this sitting '
                                                                         '(LV25A-19)')],
                                  'sheviit_gather_wood_stones_own_field': [('ordained_from_each_others_without_favor',
                                                                            None,
                                                                            'Mishnah Sheviit 4:1 — '
                                                                            'when transgressors '
                                                                            'multiplied they '
                                                                            'ordained; seat: the '
                                                                            'labor census and the '
                                                                            'class rule '
                                                                            '(LV25A-04), the '
                                                                            'thirty-day addition '
                                                                            'on the onset timeline '
                                                                            '(LV25A-02), the '
                                                                            'rooting rule '
                                                                            '(LV25A-03); the '
                                                                            "Talmud's LAYER label "
                                                                            'seated this sitting '
                                                                            '(LV25A-19)')],
                                  'sheviit_thorn_cleared_field_after': [('may_be_sown',
                                                                         None,
                                                                         'Mishnah Sheviit 4:2 — a '
                                                                         'field cleared of thorns; '
                                                                         'seat: the labor census '
                                                                         'and the class rule '
                                                                         '(LV25A-04), the '
                                                                         'thirty-day addition on '
                                                                         'the onset timeline '
                                                                         '(LV25A-02), the rooting '
                                                                         'rule (LV25A-03); the '
                                                                         "Talmud's LAYER label "
                                                                         'seated this sitting '
                                                                         '(LV25A-19)')],
                                  'sheviit_produce_eaten_as_favor': [('beit_shammai_not',
                                                                      'Beit Shammai',
                                                                      'Mishnah Sheviit 4:2 — '
                                                                      'seventh produce as a favor; '
                                                                      'seat: the labor census and '
                                                                      'the class rule (LV25A-04), '
                                                                      'the thirty-day addition on '
                                                                      'the onset timeline '
                                                                      '(LV25A-02), the rooting '
                                                                      'rule (LV25A-03); the '
                                                                      "Talmud's LAYER label seated "
                                                                      'this sitting (LV25A-19)'),
                                                                     ('beit_hillel_with_and_without',
                                                                      'Beit Hillel',
                                                                      'Mishnah Sheviit 4:2 — '
                                                                      'seventh produce as a favor; '
                                                                      'seat: the labor census and '
                                                                      'the class rule (LV25A-04), '
                                                                      'the thirty-day addition on '
                                                                      'the onset timeline '
                                                                      '(LV25A-02), the rooting '
                                                                      'rule (LV25A-03); the '
                                                                      "Talmud's LAYER label seated "
                                                                      'this sitting (LV25A-19)')],
                                  'sheviit_lease_plowed_from_gentiles': [('permitted_not_from_israelites',
                                                                          None,
                                                                          'Mishnah Sheviit 4:3 — '
                                                                          'they lease plowed '
                                                                          'fields from gentiles; '
                                                                          'seat: the labor census '
                                                                          'and the class rule '
                                                                          '(LV25A-04), the '
                                                                          'thirty-day addition on '
                                                                          'the onset timeline '
                                                                          '(LV25A-02), the rooting '
                                                                          'rule (LV25A-03); the '
                                                                          "Talmud's LAYER label "
                                                                          'seated this sitting '
                                                                          '(LV25A-19)')],
                                  'sheviit_thinning_olives': [('beit_shammai_cut',
                                                               'Beit Shammai',
                                                               'Mishnah Sheviit 4:4 — one thinning '
                                                               'olives; seat: the labor census and '
                                                               'the class rule (LV25A-04), the '
                                                               'thirty-day addition on the onset '
                                                               'timeline (LV25A-02), the rooting '
                                                               "rule (LV25A-03); the Talmud's "
                                                               'LAYER label seated this sitting '
                                                               '(LV25A-19)'),
                                                              ('beit_hillel_uproot',
                                                               'Beit Hillel',
                                                               'Mishnah Sheviit 4:4 — one thinning '
                                                               'olives; seat: the labor census and '
                                                               'the class rule (LV25A-04), the '
                                                               'thirty-day addition on the onset '
                                                               'timeline (LV25A-02), the rooting '
                                                               "rule (LV25A-03); the Talmud's "
                                                               'LAYER label seated this sitting '
                                                               '(LV25A-19)')],
                                  'sheviit_virgin_sycamore_cut': [('forbidden_it_is_labor',
                                                                   None,
                                                                   'Mishnah Sheviit 4:5 — no '
                                                                   'cutting a virgin sycamore; '
                                                                   'seat: the labor census and the '
                                                                   'class rule (LV25A-04), the '
                                                                   'thirty-day addition on the '
                                                                   'onset timeline (LV25A-02), the '
                                                                   'rooting rule (LV25A-03); the '
                                                                   "Talmud's LAYER label seated "
                                                                   'this sitting (LV25A-19)')],
                                  'sheviit_trimming_vines_cutting_reeds': [('r_yosei_hagelili_handbreadth',
                                                                            'R. Yosei HaGelili',
                                                                            'Mishnah Sheviit 4:6 — '
                                                                            'one trimming vines; '
                                                                            'seat: the labor '
                                                                            'census and the class '
                                                                            'rule (LV25A-04), the '
                                                                            'thirty-day addition '
                                                                            'on the onset timeline '
                                                                            '(LV25A-02), the '
                                                                            'rooting rule '
                                                                            '(LV25A-03); the '
                                                                            "Talmud's LAYER label "
                                                                            'seated this sitting '
                                                                            '(LV25A-19)'),
                                                                           ('r_akiva_as_usual',
                                                                            'R. Akiva',
                                                                            'Mishnah Sheviit 4:6 — '
                                                                            'one trimming vines; '
                                                                            'seat: the labor '
                                                                            'census and the class '
                                                                            'rule (LV25A-04), the '
                                                                            'thirty-day addition '
                                                                            'on the onset timeline '
                                                                            '(LV25A-02), the '
                                                                            'rooting rule '
                                                                            '(LV25A-03); the '
                                                                            "Talmud's LAYER label "
                                                                            'seated this sitting '
                                                                            '(LV25A-19)')],
                                  'sheviit_cutting_fruit_tree_when_banned': [('beit_shammai_from_budding',
                                                                              'Beit Shammai',
                                                                              'Mishnah Sheviit '
                                                                              '4:10 — from when '
                                                                              'may the tree not be '
                                                                              'cut; seat: the '
                                                                              'labor census and '
                                                                              'the class rule '
                                                                              '(LV25A-04), the '
                                                                              'thirty-day addition '
                                                                              'on the onset '
                                                                              'timeline '
                                                                              '(LV25A-02), the '
                                                                              'rooting rule '
                                                                              '(LV25A-03); the '
                                                                              "Talmud's LAYER "
                                                                              'label seated this '
                                                                              'sitting (LV25A-19)'),
                                                                             ('beit_hillel_by_species',
                                                                              'Beit Hillel',
                                                                              'Mishnah Sheviit '
                                                                              '4:10 — from when '
                                                                              'may the tree not be '
                                                                              'cut; seat: the '
                                                                              'labor census and '
                                                                              'the class rule '
                                                                              '(LV25A-04), the '
                                                                              'thirty-day addition '
                                                                              'on the onset '
                                                                              'timeline '
                                                                              '(LV25A-02), the '
                                                                              'rooting rule '
                                                                              '(LV25A-03); the '
                                                                              "Talmud's LAYER "
                                                                              'label seated this '
                                                                              'sitting '
                                                                              '(LV25A-19)')],
                                  'sheviit_derivative_labors_layer': [('rabbinic_verse_as_support',
                                                                       None,
                                                                       'Babylonian Talmud Moed '
                                                                       'Katan 3a:9 — rabbinic, and '
                                                                       'the verse a mere support; '
                                                                       'seat: the labor census and '
                                                                       'the class rule (LV25A-04), '
                                                                       'the thirty-day addition on '
                                                                       'the onset timeline '
                                                                       '(LV25A-02), the rooting '
                                                                       'rule (LV25A-03); the '
                                                                       "Talmud's LAYER label "
                                                                       'seated this sitting '
                                                                       '(LV25A-19)')],
                                  'sheviit_torah_labors': [('sow_prune_reap_gather',
                                                            None,
                                                            'Babylonian Talmud Moed Katan 3a:1 — '
                                                            'your field you shall not sow, your '
                                                            'vineyard not prune; seat: the labor '
                                                            'census and the class rule (LV25A-04), '
                                                            'the thirty-day addition on the onset '
                                                            'timeline (LV25A-02), the rooting rule '
                                                            "(LV25A-03); the Talmud's LAYER label "
                                                            'seated this sitting (LV25A-19)')],
                                  'sheviit_plowing_lashes': [('lashes',
                                                              'R. Yochanan or R. Elazar (one each '
                                                              'way)',
                                                              'Babylonian Talmud Moed Katan 3a:12 '
                                                              '— one who plows in the seventh; '
                                                              'seat: the labor census and the '
                                                              'class rule (LV25A-04), the '
                                                              'thirty-day addition on the onset '
                                                              'timeline (LV25A-02), the rooting '
                                                              "rule (LV25A-03); the Talmud's LAYER "
                                                              'label seated this sitting '
                                                              '(LV25A-19)'),
                                                             ('no_lashes',
                                                              'R. Elazar or R. Yochanan (one each '
                                                              'way)',
                                                              'Babylonian Talmud Moed Katan 3a:12 '
                                                              '— one who plows in the seventh; '
                                                              'seat: the labor census and the '
                                                              'class rule (LV25A-04), the '
                                                              'thirty-day addition on the onset '
                                                              'timeline (LV25A-02), the rooting '
                                                              "rule (LV25A-03); the Talmud's LAYER "
                                                              'label seated this sitting '
                                                              '(LV25A-19)')],
                                  'sheviit_two_hoeings': [('strengthen_barred_close_cracks_permitted',
                                                           None,
                                                           'Babylonian Talmud Moed Katan 3a:11 — '
                                                           'there are two hoeings; seat: the labor '
                                                           'census and the class rule (LV25A-04), '
                                                           'the thirty-day addition on the onset '
                                                           'timeline (LV25A-02), the rooting rule '
                                                           "(LV25A-03); the Talmud's LAYER label "
                                                           'seated this sitting (LV25A-19)')],
                                  'sheviit_addition_layers': [('thirty_days_halakhah_cutoffs_ordained',
                                                               None,
                                                               'Babylonian Talmud Moed Katan 3b:12 '
                                                               '— thirty days before the New Year; '
                                                               'seat: the labor census and the '
                                                               'class rule (LV25A-04), the '
                                                               'thirty-day addition on the onset '
                                                               'timeline (LV25A-02), the rooting '
                                                               "rule (LV25A-03); the Talmud's "
                                                               'LAYER label seated this sitting '
                                                               '(LV25A-19)')],
                                  'sheviit_cutoffs_abolished': [('rabban_gamliel_court_by_stipulation',
                                                                 None,
                                                                 'Babylonian Talmud Moed Katan '
                                                                 '3b:8 — voted on these two '
                                                                 'periods and abolished them; '
                                                                 'seat: the labor census and the '
                                                                 'class rule (LV25A-04), the '
                                                                 'thirty-day addition on the onset '
                                                                 'timeline (LV25A-02), the rooting '
                                                                 "rule (LV25A-03); the Talmud's "
                                                                 'LAYER label seated this sitting '
                                                                 '(LV25A-19)')],
                                  'sheviit_addition_temple_dependency': [('only_while_temple_stands',
                                                                          None,
                                                                          'Babylonian Talmud Moed '
                                                                          'Katan 4a:9 — while the '
                                                                          'Temple stands; seat: '
                                                                          'the labor census and '
                                                                          'the class rule '
                                                                          '(LV25A-04), the '
                                                                          'thirty-day addition on '
                                                                          'the onset timeline '
                                                                          '(LV25A-02), the rooting '
                                                                          'rule (LV25A-03); the '
                                                                          "Talmud's LAYER label "
                                                                          'seated this sitting '
                                                                          '(LV25A-19)')]}},
 'sheviit_produce_file': {'tractate': 'Sheviit',
                          'oracle': 'Mishnah Sheviit 4:7; 4:8; 4:9; 5:1; 5:2; 5:3; 5:4; 5:5; 5:6; '
                                    '5:7; 5:8; 5:9; 6:1; 6:2; 6:3; 6:4; 6:5; 7:1; 7:2; 7:3; 7:4; '
                                    '7:5; 7:6; 7:7; 8:1; 8:2; 8:3; 8:4; 8:5; 8:6; 8:7; 8:8; 8:9; '
                                    '8:11; 9:1',
                          'claim': 'LV25A-05',
                          'anchor': 'Lev.25.5-7 (lev_25_shemittah, LV25A-05, LV25A-06, LV25A-07, '
                                    'LV25A-12, LV25A-17, LV25A-18)',
                          'cells': {'sheviit_unripe_figs_eaten_when': [('glisten_field_ripened_house',
                                                                        None,
                                                                        'Mishnah Sheviit 4:7 — '
                                                                        'unripe figs from when '
                                                                        'they glisten; seat: the '
                                                                        'changed manner and the '
                                                                        'two clocks (LV25A-05), '
                                                                        'the eaters (LV25A-06), '
                                                                        'the field-clock and the '
                                                                        'season table (LV25A-07), '
                                                                        'the substitution chain '
                                                                        '(LV25A-12), the '
                                                                        "aftergrowth ban's "
                                                                        'provenance (LV25A-17), '
                                                                        "the blessing's arithmetic "
                                                                        '(LV25A-18)')],
                                    'sheviit_grapes_eaten_when': [('juice_field_soured_house',
                                                                   None,
                                                                   'Mishnah Sheviit 4:8 — unripe '
                                                                   'grapes from when they hold '
                                                                   'juice; seat: the changed '
                                                                   'manner and the two clocks '
                                                                   '(LV25A-05), the eaters '
                                                                   '(LV25A-06), the field-clock '
                                                                   'and the season table '
                                                                   '(LV25A-07), the substitution '
                                                                   'chain (LV25A-12), the '
                                                                   "aftergrowth ban's provenance "
                                                                   "(LV25A-17), the blessing's "
                                                                   'arithmetic (LV25A-18)')],
                                    'sheviit_olives_eaten_when': [('quarter_log_field_third_house',
                                                                   None,
                                                                   'Mishnah Sheviit 4:9 — from '
                                                                   'when they yield a quarter-log '
                                                                   'to the seah; seat: the changed '
                                                                   'manner and the two clocks '
                                                                   '(LV25A-05), the eaters '
                                                                   '(LV25A-06), the field-clock '
                                                                   'and the season table '
                                                                   '(LV25A-07), the substitution '
                                                                   'chain (LV25A-12), the '
                                                                   "aftergrowth ban's provenance "
                                                                   "(LV25A-17), the blessing's "
                                                                   'arithmetic (LV25A-18)')],
                                    'sheviit_other_fruit_season_rule': [('as_tithe_season',
                                                                         None,
                                                                         'Mishnah Sheviit 4:9 — as '
                                                                         'their tithe season; '
                                                                         'seat: the changed manner '
                                                                         'and the two clocks '
                                                                         '(LV25A-05), the eaters '
                                                                         '(LV25A-06), the '
                                                                         'field-clock and the '
                                                                         'season table (LV25A-07), '
                                                                         'the substitution chain '
                                                                         '(LV25A-12), the '
                                                                         "aftergrowth ban's "
                                                                         'provenance (LV25A-17), '
                                                                         "the blessing's "
                                                                         'arithmetic (LV25A-18)')],
                                    'sheviit_white_figs_year': [('second_year',
                                                                 None,
                                                                 'Mishnah Sheviit 5:1 — white figs '
                                                                 '— their seventh is the second; '
                                                                 'seat: the changed manner and the '
                                                                 'two clocks (LV25A-05), the '
                                                                 'eaters (LV25A-06), the '
                                                                 'field-clock and the season table '
                                                                 '(LV25A-07), the substitution '
                                                                 'chain (LV25A-12), the '
                                                                 "aftergrowth ban's provenance "
                                                                 "(LV25A-17), the blessing's "
                                                                 'arithmetic (LV25A-18)')],
                                    'sheviit_burying_arum_measure': [('r_meir_two_seahs',
                                                                      'R. Meir',
                                                                      'Mishnah Sheviit 5:2 — one '
                                                                      'burying arum; seat: the '
                                                                      'changed manner and the two '
                                                                      'clocks (LV25A-05), the '
                                                                      'eaters (LV25A-06), the '
                                                                      'field-clock and the season '
                                                                      'table (LV25A-07), the '
                                                                      'substitution chain '
                                                                      '(LV25A-12), the aftergrowth '
                                                                      "ban's provenance "
                                                                      "(LV25A-17), the blessing's "
                                                                      'arithmetic (LV25A-18)'),
                                                                     ('sages_four_kabs',
                                                                      'the Sages',
                                                                      'Mishnah Sheviit 5:2 — one '
                                                                      'burying arum; seat: the '
                                                                      'changed manner and the two '
                                                                      'clocks (LV25A-05), the '
                                                                      'eaters (LV25A-06), the '
                                                                      'field-clock and the season '
                                                                      'table (LV25A-07), the '
                                                                      'substitution chain '
                                                                      '(LV25A-12), the aftergrowth '
                                                                      "ban's provenance "
                                                                      "(LV25A-17), the blessing's "
                                                                      'arithmetic (LV25A-18)')],
                                    'sheviit_arum_after_seventh_poor': [('r_eliezer_reckons',
                                                                         'R. Eliezer',
                                                                         'Mishnah Sheviit 5:3 — he '
                                                                         'reckons with the poor; '
                                                                         'seat: the changed manner '
                                                                         'and the two clocks '
                                                                         '(LV25A-05), the eaters '
                                                                         '(LV25A-06), the '
                                                                         'field-clock and the '
                                                                         'season table (LV25A-07), '
                                                                         'the substitution chain '
                                                                         '(LV25A-12), the '
                                                                         "aftergrowth ban's "
                                                                         'provenance (LV25A-17), '
                                                                         "the blessing's "
                                                                         'arithmetic (LV25A-18)'),
                                                                        ('r_yehoshua_no_reckoning',
                                                                         'R. Yehoshua',
                                                                         'Mishnah Sheviit 5:3 — he '
                                                                         'reckons with the poor; '
                                                                         'seat: the changed manner '
                                                                         'and the two clocks '
                                                                         '(LV25A-05), the eaters '
                                                                         '(LV25A-06), the '
                                                                         'field-clock and the '
                                                                         'season table (LV25A-07), '
                                                                         'the substitution chain '
                                                                         '(LV25A-12), the '
                                                                         "aftergrowth ban's "
                                                                         'provenance (LV25A-17), '
                                                                         "the blessing's "
                                                                         'arithmetic (LV25A-18)')],
                                    'sheviit_arum_eve_uprooting_tool': [('beit_shammai_wooden',
                                                                         'Beit Shammai',
                                                                         'Mishnah Sheviit 5:4 — '
                                                                         'with wooden rakes; seat: '
                                                                         'the changed manner and '
                                                                         'the two clocks '
                                                                         '(LV25A-05), the eaters '
                                                                         '(LV25A-06), the '
                                                                         'field-clock and the '
                                                                         'season table (LV25A-07), '
                                                                         'the substitution chain '
                                                                         '(LV25A-12), the '
                                                                         "aftergrowth ban's "
                                                                         'provenance (LV25A-17), '
                                                                         "the blessing's "
                                                                         'arithmetic (LV25A-18)'),
                                                                        ('beit_hillel_metal',
                                                                         'Beit Hillel',
                                                                         'Mishnah Sheviit 5:4 — '
                                                                         'with wooden rakes; seat: '
                                                                         'the changed manner and '
                                                                         'the two clocks '
                                                                         '(LV25A-05), the eaters '
                                                                         '(LV25A-06), the '
                                                                         'field-clock and the '
                                                                         'season table (LV25A-07), '
                                                                         'the substitution chain '
                                                                         '(LV25A-12), the '
                                                                         "aftergrowth ban's "
                                                                         'provenance (LV25A-17), '
                                                                         "the blessing's "
                                                                         'arithmetic (LV25A-18)')],
                                    'sheviit_buying_arum_after': [('r_yehuda_at_once',
                                                                   'R. Yehuda',
                                                                   'Mishnah Sheviit 5:5 — when the '
                                                                   'new is plentiful; seat: the '
                                                                   'changed manner and the two '
                                                                   'clocks (LV25A-05), the eaters '
                                                                   '(LV25A-06), the field-clock '
                                                                   'and the season table '
                                                                   '(LV25A-07), the substitution '
                                                                   'chain (LV25A-12), the '
                                                                   "aftergrowth ban's provenance "
                                                                   "(LV25A-17), the blessing's "
                                                                   'arithmetic (LV25A-18)'),
                                                                  ('sages_when_new_plentiful',
                                                                   'the Sages',
                                                                   'Mishnah Sheviit 5:5 — when the '
                                                                   'new is plentiful; seat: the '
                                                                   'changed manner and the two '
                                                                   'clocks (LV25A-05), the eaters '
                                                                   '(LV25A-06), the field-clock '
                                                                   'and the season table '
                                                                   '(LV25A-07), the substitution '
                                                                   'chain (LV25A-12), the '
                                                                   "aftergrowth ban's provenance "
                                                                   "(LV25A-17), the blessing's "
                                                                   'arithmetic (LV25A-18)')],
                                    'sheviit_tools_sale_rule': [('work_specific_to_transgression_barred',
                                                                 None,
                                                                 'Mishnah Sheviit 5:6 — all whose '
                                                                 'work is specific to '
                                                                 'transgression; seat: the changed '
                                                                 'manner and the two clocks '
                                                                 '(LV25A-05), the eaters '
                                                                 '(LV25A-06), the field-clock and '
                                                                 'the season table (LV25A-07), the '
                                                                 'substitution chain (LV25A-12), '
                                                                 "the aftergrowth ban's provenance "
                                                                 "(LV25A-17), the blessing's "
                                                                 'arithmetic (LV25A-18)')],
                                    'sheviit_potter_jars': [('five_oil_fifteen_wine',
                                                             None,
                                                             'Mishnah Sheviit 5:7 — five oil jars '
                                                             'and fifteen wine jars; seat: the '
                                                             'changed manner and the two clocks '
                                                             '(LV25A-05), the eaters (LV25A-06), '
                                                             'the field-clock and the season table '
                                                             '(LV25A-07), the substitution chain '
                                                             "(LV25A-12), the aftergrowth ban's "
                                                             'provenance (LV25A-17), the '
                                                             "blessing's arithmetic (LV25A-18)")],
                                    'sheviit_plowing_cow_to_suspect': [('beit_shammai_forbidden',
                                                                        'Beit Shammai',
                                                                        'Mishnah Sheviit 5:8 — he '
                                                                        'may not sell him a '
                                                                        'plowing cow; seat: the '
                                                                        'changed manner and the '
                                                                        'two clocks (LV25A-05), '
                                                                        'the eaters (LV25A-06), '
                                                                        'the field-clock and the '
                                                                        'season table (LV25A-07), '
                                                                        'the substitution chain '
                                                                        '(LV25A-12), the '
                                                                        "aftergrowth ban's "
                                                                        'provenance (LV25A-17), '
                                                                        "the blessing's arithmetic "
                                                                        '(LV25A-18)'),
                                                                       ('beit_hillel_can_slaughter',
                                                                        'Beit Hillel',
                                                                        'Mishnah Sheviit 5:8 — he '
                                                                        'may not sell him a '
                                                                        'plowing cow; seat: the '
                                                                        'changed manner and the '
                                                                        'two clocks (LV25A-05), '
                                                                        'the eaters (LV25A-06), '
                                                                        'the field-clock and the '
                                                                        'season table (LV25A-07), '
                                                                        'the substitution chain '
                                                                        '(LV25A-12), the '
                                                                        "aftergrowth ban's "
                                                                        'provenance (LV25A-17), '
                                                                        "the blessing's arithmetic "
                                                                        '(LV25A-18)')],
                                    'sheviit_sale_to_suspect_explicit': [('forbidden',
                                                                          None,
                                                                          'Mishnah Sheviit 5:8 — '
                                                                          'all of them, '
                                                                          'explicitly, forbidden; '
                                                                          'seat: the changed '
                                                                          'manner and the two '
                                                                          'clocks (LV25A-05), the '
                                                                          'eaters (LV25A-06), the '
                                                                          'field-clock and the '
                                                                          'season table '
                                                                          '(LV25A-07), the '
                                                                          'substitution chain '
                                                                          '(LV25A-12), the '
                                                                          "aftergrowth ban's "
                                                                          'provenance (LV25A-17), '
                                                                          "the blessing's "
                                                                          'arithmetic (LV25A-18)')],
                                    'sheviit_lending_sieve_to_suspect': [('permitted_ways_of_peace',
                                                                          None,
                                                                          'Mishnah Sheviit 5:9 — a '
                                                                          'woman lends her '
                                                                          'neighbor; seat: the '
                                                                          'changed manner and the '
                                                                          'two clocks (LV25A-05), '
                                                                          'the eaters (LV25A-06), '
                                                                          'the field-clock and the '
                                                                          'season table '
                                                                          '(LV25A-07), the '
                                                                          'substitution chain '
                                                                          '(LV25A-12), the '
                                                                          "aftergrowth ban's "
                                                                          'provenance (LV25A-17), '
                                                                          "the blessing's "
                                                                          'arithmetic (LV25A-18)')],
                                    'sheviit_helping_after_water_added': [('forbidden',
                                                                           None,
                                                                           'Mishnah Sheviit 5:9 — '
                                                                           'once she adds water '
                                                                           'she may not touch; '
                                                                           'seat: the changed '
                                                                           'manner and the two '
                                                                           'clocks (LV25A-05), the '
                                                                           'eaters (LV25A-06), the '
                                                                           'field-clock and the '
                                                                           'season table '
                                                                           '(LV25A-07), the '
                                                                           'substitution chain '
                                                                           '(LV25A-12), the '
                                                                           "aftergrowth ban's "
                                                                           'provenance (LV25A-17), '
                                                                           "the blessing's "
                                                                           'arithmetic '
                                                                           '(LV25A-18)')],
                                    'sheviit_three_lands': [('babylon_egypt_beyond',
                                                             None,
                                                             'Mishnah Sheviit 6:1 — three lands '
                                                             'for the seventh; seat: the changed '
                                                             'manner and the two clocks '
                                                             '(LV25A-05), the eaters (LV25A-06), '
                                                             'the field-clock and the season table '
                                                             '(LV25A-07), the substitution chain '
                                                             "(LV25A-12), the aftergrowth ban's "
                                                             'provenance (LV25A-17), the '
                                                             "blessing's arithmetic (LV25A-18)")],
                                    'sheviit_syria_work': [('detached_yes_attached_no',
                                                            None,
                                                            'Mishnah Sheviit 6:2 — they work '
                                                            'detached produce in Syria; seat: the '
                                                            'changed manner and the two clocks '
                                                            '(LV25A-05), the eaters (LV25A-06), '
                                                            'the field-clock and the season table '
                                                            '(LV25A-07), the substitution chain '
                                                            "(LV25A-12), the aftergrowth ban's "
                                                            "provenance (LV25A-17), the blessing's "
                                                            'arithmetic (LV25A-18)')],
                                    'sheviit_onions_sprouted_after_rain': [('black_forbidden_green_permitted',
                                                                            None,
                                                                            'Mishnah Sheviit 6:3 — '
                                                                            'if their leaves were '
                                                                            'black; seat: the '
                                                                            'changed manner and '
                                                                            'the two clocks '
                                                                            '(LV25A-05), the '
                                                                            'eaters (LV25A-06), '
                                                                            'the field-clock and '
                                                                            'the season table '
                                                                            '(LV25A-07), the '
                                                                            'substitution chain '
                                                                            '(LV25A-12), the '
                                                                            "aftergrowth ban's "
                                                                            'provenance '
                                                                            '(LV25A-17), the '
                                                                            "blessing's arithmetic "
                                                                            '(LV25A-18)')],
                                    'sheviit_buying_greens_after': [('when_like_has_grown',
                                                                     None,
                                                                     'Mishnah Sheviit 6:4 — when '
                                                                     'its like has grown; seat: '
                                                                     'the changed manner and the '
                                                                     'two clocks (LV25A-05), the '
                                                                     'eaters (LV25A-06), the '
                                                                     'field-clock and the season '
                                                                     'table (LV25A-07), the '
                                                                     'substitution chain '
                                                                     '(LV25A-12), the aftergrowth '
                                                                     "ban's provenance (LV25A-17), "
                                                                     "the blessing's arithmetic "
                                                                     '(LV25A-18)')],
                                    'sheviit_export_abroad': [('forbidden_syria_permitted',
                                                               None,
                                                               'Mishnah Sheviit 6:5 — not exported '
                                                               'from the land abroad; seat: the '
                                                               'changed manner and the two clocks '
                                                               '(LV25A-05), the eaters (LV25A-06), '
                                                               'the field-clock and the season '
                                                               'table (LV25A-07), the substitution '
                                                               'chain (LV25A-12), the aftergrowth '
                                                               "ban's provenance (LV25A-17), the "
                                                               "blessing's arithmetic (LV25A-18)")],
                                    'sheviit_great_rule_sanctity_removal': [('food_dye_not_enduring_both',
                                                                             None,
                                                                             'Mishnah Sheviit 7:1 '
                                                                             '— a great rule they '
                                                                             'stated for the '
                                                                             'seventh; seat: the '
                                                                             'changed manner and '
                                                                             'the two clocks '
                                                                             '(LV25A-05), the '
                                                                             'eaters (LV25A-06), '
                                                                             'the field-clock and '
                                                                             'the season table '
                                                                             '(LV25A-07), the '
                                                                             'substitution chain '
                                                                             '(LV25A-12), the '
                                                                             "aftergrowth ban's "
                                                                             'provenance '
                                                                             '(LV25A-17), the '
                                                                             "blessing's "
                                                                             'arithmetic '
                                                                             '(LV25A-18)')],
                                    'sheviit_enduring_in_ground': [('sanctity_no_removal',
                                                                    None,
                                                                    'Mishnah Sheviit 7:2 — and '
                                                                    'endures in the ground; seat: '
                                                                    'the changed manner and the '
                                                                    'two clocks (LV25A-05), the '
                                                                    'eaters (LV25A-06), the '
                                                                    'field-clock and the season '
                                                                    'table (LV25A-07), the '
                                                                    'substitution chain '
                                                                    '(LV25A-12), the aftergrowth '
                                                                    "ban's provenance (LV25A-17), "
                                                                    "the blessing's arithmetic "
                                                                    '(LV25A-18)')],
                                    'sheviit_commerce_in_produce': [('barred',
                                                                     None,
                                                                     'Mishnah Sheviit 7:3 — no '
                                                                     'commerce in seventh produce; '
                                                                     'seat: the changed manner and '
                                                                     'the two clocks (LV25A-05), '
                                                                     'the eaters (LV25A-06), the '
                                                                     'field-clock and the season '
                                                                     'table (LV25A-07), the '
                                                                     'substitution chain '
                                                                     '(LV25A-12), the aftergrowth '
                                                                     "ban's provenance (LV25A-17), "
                                                                     "the blessing's arithmetic "
                                                                     '(LV25A-18)')],
                                    'sheviit_gathered_greens_sold_by_son': [('permitted',
                                                                             None,
                                                                             'Mishnah Sheviit 7:3 '
                                                                             '— he gathers and his '
                                                                             'son sells; seat: the '
                                                                             'changed manner and '
                                                                             'the two clocks '
                                                                             '(LV25A-05), the '
                                                                             'eaters (LV25A-06), '
                                                                             'the field-clock and '
                                                                             'the season table '
                                                                             '(LV25A-07), the '
                                                                             'substitution chain '
                                                                             '(LV25A-12), the '
                                                                             "aftergrowth ban's "
                                                                             'provenance '
                                                                             '(LV25A-17), the '
                                                                             "blessing's "
                                                                             'arithmetic '
                                                                             '(LV25A-18)')],
                                    'sheviit_chanced_impure_kinds_sale': [('r_yehuda_casual_permitted',
                                                                           'R. Yehuda',
                                                                           'Mishnah Sheviit 7:4 — '
                                                                           'one who chanced on '
                                                                           'them casually; seat: '
                                                                           'the changed manner and '
                                                                           'the two clocks '
                                                                           '(LV25A-05), the eaters '
                                                                           '(LV25A-06), the '
                                                                           'field-clock and the '
                                                                           'season table '
                                                                           '(LV25A-07), the '
                                                                           'substitution chain '
                                                                           '(LV25A-12), the '
                                                                           "aftergrowth ban's "
                                                                           'provenance (LV25A-17), '
                                                                           "the blessing's "
                                                                           'arithmetic (LV25A-18)'),
                                                                          ('sages_forbid',
                                                                           'the Sages',
                                                                           'Mishnah Sheviit 7:4 — '
                                                                           'one who chanced on '
                                                                           'them casually; seat: '
                                                                           'the changed manner and '
                                                                           'the two clocks '
                                                                           '(LV25A-05), the eaters '
                                                                           '(LV25A-06), the '
                                                                           'field-clock and the '
                                                                           'season table '
                                                                           '(LV25A-07), the '
                                                                           'substitution chain '
                                                                           '(LV25A-12), the '
                                                                           "aftergrowth ban's "
                                                                           'provenance (LV25A-17), '
                                                                           "the blessing's "
                                                                           'arithmetic '
                                                                           '(LV25A-18)')],
                                    'sheviit_sprouts_removal': [('zeradim_carobs_yes_terebinth_no',
                                                                 None,
                                                                 'Mishnah Sheviit 7:5 — sprouts of '
                                                                 'the shoot-tree and carobs; seat: '
                                                                 'the changed manner and the two '
                                                                 'clocks (LV25A-05), the eaters '
                                                                 '(LV25A-06), the field-clock and '
                                                                 'the season table (LV25A-07), the '
                                                                 'substitution chain (LV25A-12), '
                                                                 "the aftergrowth ban's provenance "
                                                                 "(LV25A-17), the blessing's "
                                                                 'arithmetic (LV25A-18)')],
                                    'sheviit_balsam_sanctity': [('sanctity',
                                                                 'the first Tanna',
                                                                 'Mishnah Sheviit 7:6 — balsam has '
                                                                 'no seventh-sanctity; seat: the '
                                                                 'changed manner and the two '
                                                                 'clocks (LV25A-05), the eaters '
                                                                 '(LV25A-06), the field-clock and '
                                                                 'the season table (LV25A-07), the '
                                                                 'substitution chain (LV25A-12), '
                                                                 "the aftergrowth ban's provenance "
                                                                 "(LV25A-17), the blessing's "
                                                                 'arithmetic (LV25A-18)'),
                                                                ('r_shimon_none_not_fruit',
                                                                 'R. Shimon',
                                                                 'Mishnah Sheviit 7:6 — balsam has '
                                                                 'no seventh-sanctity; seat: the '
                                                                 'changed manner and the two '
                                                                 'clocks (LV25A-05), the eaters '
                                                                 '(LV25A-06), the field-clock and '
                                                                 'the season table (LV25A-07), the '
                                                                 'substitution chain (LV25A-12), '
                                                                 "the aftergrowth ban's provenance "
                                                                 "(LV25A-17), the blessing's "
                                                                 'arithmetic (LV25A-18)')],
                                    'sheviit_mixture_rule': [('taste_other_kind_any_amount_same_kind',
                                                              None,
                                                              'Mishnah Sheviit 7:7 — whatever '
                                                              'imparts taste; seat: the changed '
                                                              'manner and the two clocks '
                                                              '(LV25A-05), the eaters (LV25A-06), '
                                                              'the field-clock and the season '
                                                              'table (LV25A-07), the substitution '
                                                              'chain (LV25A-12), the aftergrowth '
                                                              "ban's provenance (LV25A-17), the "
                                                              "blessing's arithmetic (LV25A-18)")],
                                    'sheviit_poultice_rule': [('human_food_none_other_for_man_intent_decides',
                                                               None,
                                                               'Mishnah Sheviit 8:1 — no poultice '
                                                               'is made from it; seat: the changed '
                                                               'manner and the two clocks '
                                                               '(LV25A-05), the eaters (LV25A-06), '
                                                               'the field-clock and the season '
                                                               'table (LV25A-07), the substitution '
                                                               'chain (LV25A-12), the aftergrowth '
                                                               "ban's provenance (LV25A-17), the "
                                                               "blessing's arithmetic (LV25A-18)")],
                                    'sheviit_produce_uses': [('eating_drinking_anointing_lamp',
                                                              None,
                                                              'Mishnah Sheviit 8:2 — given for '
                                                              'eating, drinking, and anointing; '
                                                              'seat: the changed manner and the '
                                                              'two clocks (LV25A-05), the eaters '
                                                              '(LV25A-06), the field-clock and the '
                                                              'season table (LV25A-07), the '
                                                              'substitution chain (LV25A-12), the '
                                                              "aftergrowth ban's provenance "
                                                              "(LV25A-17), the blessing's "
                                                              'arithmetic (LV25A-18)')],
                                    'sheviit_sale_by_measure': [('forbidden',
                                                                 None,
                                                                 'Mishnah Sheviit 8:3 — not by '
                                                                 'measure, weight, or number; '
                                                                 'seat: the changed manner and the '
                                                                 'two clocks (LV25A-05), the '
                                                                 'eaters (LV25A-06), the '
                                                                 'field-clock and the season table '
                                                                 '(LV25A-07), the substitution '
                                                                 'chain (LV25A-12), the '
                                                                 "aftergrowth ban's provenance "
                                                                 "(LV25A-17), the blessing's "
                                                                 'arithmetic (LV25A-18)')],
                                    'sheviit_sale_in_bundles': [('beit_shammai_not',
                                                                 'Beit Shammai',
                                                                 'Mishnah Sheviit 8:3 — not even '
                                                                 'in bundles; seat: the changed '
                                                                 'manner and the two clocks '
                                                                 '(LV25A-05), the eaters '
                                                                 '(LV25A-06), the field-clock and '
                                                                 'the season table (LV25A-07), the '
                                                                 'substitution chain (LV25A-12), '
                                                                 "the aftergrowth ban's provenance "
                                                                 "(LV25A-17), the blessing's "
                                                                 'arithmetic (LV25A-18)'),
                                                                ('beit_hillel_home_bundled',
                                                                 'Beit Hillel',
                                                                 'Mishnah Sheviit 8:3 — not even '
                                                                 'in bundles; seat: the changed '
                                                                 'manner and the two clocks '
                                                                 '(LV25A-05), the eaters '
                                                                 '(LV25A-06), the field-clock and '
                                                                 'the season table (LV25A-07), the '
                                                                 'substitution chain (LV25A-12), '
                                                                 "the aftergrowth ban's provenance "
                                                                 "(LV25A-17), the blessing's "
                                                                 'arithmetic (LV25A-18)')],
                                    'sheviit_wage_for_gathering': [('today_permitted_for_it_forbidden',
                                                                    None,
                                                                    'Mishnah Sheviit 8:4 — take '
                                                                    'this coin and gather me '
                                                                    'greens today; seat: the '
                                                                    'changed manner and the two '
                                                                    'clocks (LV25A-05), the eaters '
                                                                    '(LV25A-06), the field-clock '
                                                                    'and the season table '
                                                                    '(LV25A-07), the substitution '
                                                                    'chain (LV25A-12), the '
                                                                    "aftergrowth ban's provenance "
                                                                    "(LV25A-17), the blessing's "
                                                                    'arithmetic (LV25A-18)')],
                                    'sheviit_debt_paid_from_produce_money': [('forbidden',
                                                                              None,
                                                                              'Mishnah Sheviit 8:4 '
                                                                              '— no debt is paid '
                                                                              'from seventh money; '
                                                                              'seat: the changed '
                                                                              'manner and the two '
                                                                              'clocks (LV25A-05), '
                                                                              'the eaters '
                                                                              '(LV25A-06), the '
                                                                              'field-clock and the '
                                                                              'season table '
                                                                              '(LV25A-07), the '
                                                                              'substitution chain '
                                                                              '(LV25A-12), the '
                                                                              "aftergrowth ban's "
                                                                              'provenance '
                                                                              '(LV25A-17), the '
                                                                              "blessing's "
                                                                              'arithmetic '
                                                                              '(LV25A-18)')],
                                    'sheviit_paying_bath_attendant': [('forbidden_free_gift_permitted',
                                                                       None,
                                                                       'Mishnah Sheviit 8:5 — not '
                                                                       'to the bath-attendant nor '
                                                                       'the barber; seat: the '
                                                                       'changed manner and the two '
                                                                       'clocks (LV25A-05), the '
                                                                       'eaters (LV25A-06), the '
                                                                       'field-clock and the season '
                                                                       'table (LV25A-07), the '
                                                                       'substitution chain '
                                                                       '(LV25A-12), the '
                                                                       "aftergrowth ban's "
                                                                       'provenance (LV25A-17), the '
                                                                       "blessing's arithmetic "
                                                                       '(LV25A-18)')],
                                    'sheviit_changed_manner_processing': [('not_press_but_trough',
                                                                           None,
                                                                           'Mishnah Sheviit 8:6 — '
                                                                           'grapes not trodden in '
                                                                           'the press; seat: the '
                                                                           'changed manner and the '
                                                                           'two clocks (LV25A-05), '
                                                                           'the eaters (LV25A-06), '
                                                                           'the field-clock and '
                                                                           'the season table '
                                                                           '(LV25A-07), the '
                                                                           'substitution chain '
                                                                           '(LV25A-12), the '
                                                                           "aftergrowth ban's "
                                                                           'provenance (LV25A-17), '
                                                                           "the blessing's "
                                                                           'arithmetic '
                                                                           '(LV25A-18)')],
                                    'sheviit_cooking_in_priestly_oil': [('forbidden_lest_disqualified',
                                                                         'the first Tanna',
                                                                         'Mishnah Sheviit 8:7 — no '
                                                                         'cooking seventh greens; '
                                                                         'seat: the changed manner '
                                                                         'and the two clocks '
                                                                         '(LV25A-05), the eaters '
                                                                         '(LV25A-06), the '
                                                                         'field-clock and the '
                                                                         'season table (LV25A-07), '
                                                                         'the substitution chain '
                                                                         '(LV25A-12), the '
                                                                         "aftergrowth ban's "
                                                                         'provenance (LV25A-17), '
                                                                         "the blessing's "
                                                                         'arithmetic (LV25A-18)'),
                                                                        ('r_shimon_permits',
                                                                         'R. Shimon',
                                                                         'Mishnah Sheviit 8:7 — no '
                                                                         'cooking seventh greens; '
                                                                         'seat: the changed manner '
                                                                         'and the two clocks '
                                                                         '(LV25A-05), the eaters '
                                                                         '(LV25A-06), the '
                                                                         'field-clock and the '
                                                                         'season table (LV25A-07), '
                                                                         'the substitution chain '
                                                                         '(LV25A-12), the '
                                                                         "aftergrowth ban's "
                                                                         'provenance (LV25A-17), '
                                                                         "the blessing's "
                                                                         'arithmetic (LV25A-18)')],
                                    'sheviit_money_chain': [('last_seized_fruit_forbidden',
                                                             None,
                                                             'Mishnah Sheviit 8:7 — and the last '
                                                             'and last is seized; seat: the '
                                                             'changed manner and the two clocks '
                                                             '(LV25A-05), the eaters (LV25A-06), '
                                                             'the field-clock and the season table '
                                                             '(LV25A-07), the substitution chain '
                                                             "(LV25A-12), the aftergrowth ban's "
                                                             'provenance (LV25A-17), the '
                                                             "blessing's arithmetic (LV25A-18)")],
                                    'sheviit_buying_land_slaves_with_money': [('forbidden_eat_corresponding',
                                                                               None,
                                                                               'Mishnah Sheviit '
                                                                               '8:8 — no buying '
                                                                               'slaves and land; '
                                                                               'seat: the changed '
                                                                               'manner and the two '
                                                                               'clocks (LV25A-05), '
                                                                               'the eaters '
                                                                               '(LV25A-06), the '
                                                                               'field-clock and '
                                                                               'the season table '
                                                                               '(LV25A-07), the '
                                                                               'substitution chain '
                                                                               '(LV25A-12), the '
                                                                               "aftergrowth ban's "
                                                                               'provenance '
                                                                               '(LV25A-17), the '
                                                                               "blessing's "
                                                                               'arithmetic '
                                                                               '(LV25A-18)')],
                                    'sheviit_hide_oiled': [('r_eliezer_burn',
                                                            'R. Eliezer',
                                                            'Mishnah Sheviit 8:9 — a hide oiled '
                                                            'with seventh oil; seat: the changed '
                                                            'manner and the two clocks (LV25A-05), '
                                                            'the eaters (LV25A-06), the '
                                                            'field-clock and the season table '
                                                            '(LV25A-07), the substitution chain '
                                                            "(LV25A-12), the aftergrowth ban's "
                                                            "provenance (LV25A-17), the blessing's "
                                                            'arithmetic (LV25A-18)'),
                                                           ('sages_eat_corresponding',
                                                            'the Sages',
                                                            'Mishnah Sheviit 8:9 — a hide oiled '
                                                            'with seventh oil; seat: the changed '
                                                            'manner and the two clocks (LV25A-05), '
                                                            'the eaters (LV25A-06), the '
                                                            'field-clock and the season table '
                                                            '(LV25A-07), the substitution chain '
                                                            "(LV25A-12), the aftergrowth ban's "
                                                            "provenance (LV25A-17), the blessing's "
                                                            'arithmetic (LV25A-18)')],
                                    'sheviit_bathhouse_heated_with_straw': [('permitted_man_of_standing_not',
                                                                             None,
                                                                             'Mishnah Sheviit 8:11 '
                                                                             '— a bathhouse heated '
                                                                             'with straw; seat: '
                                                                             'the changed manner '
                                                                             'and the two clocks '
                                                                             '(LV25A-05), the '
                                                                             'eaters (LV25A-06), '
                                                                             'the field-clock and '
                                                                             'the season table '
                                                                             '(LV25A-07), the '
                                                                             'substitution chain '
                                                                             '(LV25A-12), the '
                                                                             "aftergrowth ban's "
                                                                             'provenance '
                                                                             '(LV25A-17), the '
                                                                             "blessing's "
                                                                             'arithmetic '
                                                                             '(LV25A-18)')],
                                    'sheviit_aftergrowth': [('sages_all_forbidden',
                                                             'the Sages',
                                                             'Mishnah Sheviit 9:1 — all '
                                                             'aftergrowth forbidden; seat: the '
                                                             'changed manner and the two clocks '
                                                             '(LV25A-05), the eaters (LV25A-06), '
                                                             'the field-clock and the season table '
                                                             '(LV25A-07), the substitution chain '
                                                             "(LV25A-12), the aftergrowth ban's "
                                                             'provenance (LV25A-17), the '
                                                             "blessing's arithmetic (LV25A-18)"),
                                                            ('r_shimon_permitted_but_cabbage',
                                                             'R. Shimon',
                                                             'Mishnah Sheviit 9:1 — all '
                                                             'aftergrowth forbidden; seat: the '
                                                             'changed manner and the two clocks '
                                                             '(LV25A-05), the eaters (LV25A-06), '
                                                             'the field-clock and the season table '
                                                             '(LV25A-07), the substitution chain '
                                                             "(LV25A-12), the aftergrowth ban's "
                                                             'provenance (LV25A-17), the '
                                                             "blessing's arithmetic (LV25A-18)"),
                                                            ('r_yehuda_mustard_permitted',
                                                             'R. Yehuda',
                                                             'Mishnah Sheviit 9:1 — all '
                                                             'aftergrowth forbidden; seat: the '
                                                             'changed manner and the two clocks '
                                                             '(LV25A-05), the eaters (LV25A-06), '
                                                             'the field-clock and the season table '
                                                             '(LV25A-07), the substitution chain '
                                                             "(LV25A-12), the aftergrowth ban's "
                                                             'provenance (LV25A-17), the '
                                                             "blessing's arithmetic (LV25A-18)")],
                                    'sheviit_unguarded_herbs_bought_from_anyone': [('permitted_not_guarded',
                                                                                    None,
                                                                                    'Mishnah '
                                                                                    'Sheviit 9:1 — '
                                                                                    'for their '
                                                                                    'like is not '
                                                                                    'guarded; '
                                                                                    'seat: the '
                                                                                    'changed '
                                                                                    'manner and '
                                                                                    'the two '
                                                                                    'clocks '
                                                                                    '(LV25A-05), '
                                                                                    'the eaters '
                                                                                    '(LV25A-06), '
                                                                                    'the '
                                                                                    'field-clock '
                                                                                    'and the '
                                                                                    'season table '
                                                                                    '(LV25A-07), '
                                                                                    'the '
                                                                                    'substitution '
                                                                                    'chain '
                                                                                    '(LV25A-12), '
                                                                                    'the '
                                                                                    'aftergrowth '
                                                                                    "ban's "
                                                                                    'provenance '
                                                                                    '(LV25A-17), '
                                                                                    'the '
                                                                                    "blessing's "
                                                                                    'arithmetic '
                                                                                    '(LV25A-18)')]}},
 'sheviit_biur_file': {'tractate': 'Sheviit',
                       'oracle': 'Mishnah Sheviit 9:2; 9:3; 9:4; 9:5; 9:6; 9:7; 9:8; 9:9',
                       'claim': 'LV25A-07',
                       'anchor': 'Lev.25.6-7 (lev_25_shemittah, LV25A-06, LV25A-07, LV25A-12)',
                       'cells': {'sheviit_removal_three_lands': [('judah_transjordan_galilee',
                                                                  None,
                                                                  'Mishnah Sheviit 9:2 — three '
                                                                  'lands for the removal; seat: '
                                                                  'the eaters and the removal '
                                                                  'dispute (LV25A-06), the '
                                                                  'field-clock (LV25A-07), the jar '
                                                                  'dispute (LV25A-12)')],
                                 'sheviit_removal_why_three_lands': [('eat_until_last_in_each',
                                                                      None,
                                                                      'Mishnah Sheviit 9:3 — until '
                                                                      'the last in it is gone; '
                                                                      'seat: the eaters and the '
                                                                      'removal dispute (LV25A-06), '
                                                                      'the field-clock (LV25A-07), '
                                                                      'the jar dispute '
                                                                      '(LV25A-12)')],
                                 'sheviit_removal_olives_dates': [('all_lands_as_one',
                                                                   None,
                                                                   'Mishnah Sheviit 9:3 — as one '
                                                                   'for olives and dates; seat: '
                                                                   'the eaters and the removal '
                                                                   'dispute (LV25A-06), the '
                                                                   'field-clock (LV25A-07), the '
                                                                   'jar dispute (LV25A-12)')],
                                 'sheviit_eat_on_guarded': [('not_on_guarded',
                                                             'the first Tanna',
                                                             'Mishnah Sheviit 9:4 — eat on the '
                                                             'ownerless not the guarded; seat: the '
                                                             'eaters and the removal dispute '
                                                             '(LV25A-06), the field-clock '
                                                             '(LV25A-07), the jar dispute '
                                                             '(LV25A-12)'),
                                                            ('r_yosei_even_guarded',
                                                             'R. Yosei',
                                                             'Mishnah Sheviit 9:4 — eat on the '
                                                             'ownerless not the guarded; seat: the '
                                                             'eaters and the removal dispute '
                                                             '(LV25A-06), the field-clock '
                                                             '(LV25A-07), the jar dispute '
                                                             '(LV25A-12)')],
                                 'sheviit_three_pickled_one_jar': [('r_eliezer_on_first',
                                                                    'R. Eliezer',
                                                                    'Mishnah Sheviit 9:5 — one '
                                                                    'pickling three kinds; seat: '
                                                                    'the eaters and the removal '
                                                                    'dispute (LV25A-06), the '
                                                                    'field-clock (LV25A-07), the '
                                                                    'jar dispute (LV25A-12)'),
                                                                   ('r_yehoshua_on_last',
                                                                    'R. Yehoshua',
                                                                    'Mishnah Sheviit 9:5 — one '
                                                                    'pickling three kinds; seat: '
                                                                    'the eaters and the removal '
                                                                    'dispute (LV25A-06), the '
                                                                    'field-clock (LV25A-07), the '
                                                                    'jar dispute (LV25A-12)'),
                                                                   ('rabban_gamliel_per_kind_the_law',
                                                                    'Rabban Gamliel (the law '
                                                                    'follows him)',
                                                                    'Mishnah Sheviit 9:5 — one '
                                                                    'pickling three kinds; seat: '
                                                                    'the eaters and the removal '
                                                                    'dispute (LV25A-06), the '
                                                                    'field-clock (LV25A-07), the '
                                                                    'jar dispute (LV25A-12)')],
                                 'sheviit_gathering_grass_until': [('fresh_sweet_dries_dry_second_rain',
                                                                    None,
                                                                    'Mishnah Sheviit 9:6 — until '
                                                                    'the sweet dries; seat: the '
                                                                    'eaters and the removal '
                                                                    'dispute (LV25A-06), the '
                                                                    'field-clock (LV25A-07), the '
                                                                    'jar dispute (LV25A-12)')],
                                 'sheviit_until_the_rains_idiom': [('second_rain',
                                                                    None,
                                                                    'Mishnah Sheviit 9:7 — until '
                                                                    'the second rain falls; seat: '
                                                                    'the eaters and the removal '
                                                                    'dispute (LV25A-06), the '
                                                                    'field-clock (LV25A-07), the '
                                                                    'jar dispute (LV25A-12)')],
                                 'sheviit_removal_protocol': [('three_meals_to_each',
                                                               None,
                                                               'Mishnah Sheviit 9:8 — he '
                                                               "distributes three meals' food; "
                                                               'seat: the eaters and the removal '
                                                               'dispute (LV25A-06), the '
                                                               'field-clock (LV25A-07), the jar '
                                                               'dispute (LV25A-12)')],
                                 'sheviit_eating_after_removal': [('r_yehuda_poor_only',
                                                                   'R. Yehuda',
                                                                   'Mishnah Sheviit 9:8 — the poor '
                                                                   'eat after the removal; seat: '
                                                                   'the eaters and the removal '
                                                                   'dispute (LV25A-06), the '
                                                                   'field-clock (LV25A-07), the '
                                                                   'jar dispute (LV25A-12)'),
                                                                  ('r_yosei_poor_and_rich',
                                                                   'R. Yosei',
                                                                   'Mishnah Sheviit 9:8 — the poor '
                                                                   'eat after the removal; seat: '
                                                                   'the eaters and the removal '
                                                                   'dispute (LV25A-06), the '
                                                                   'field-clock (LV25A-07), the '
                                                                   'jar dispute (LV25A-12)')],
                                 'sheviit_produce_inherited': [('r_eliezer_to_eaters',
                                                                'R. Eliezer',
                                                                'Mishnah Sheviit 9:9 — the sinner '
                                                                'does not profit; seat: the eaters '
                                                                'and the removal dispute '
                                                                '(LV25A-06), the field-clock '
                                                                '(LV25A-07), the jar dispute '
                                                                '(LV25A-12)'),
                                                               ('sages_sold_money_divided',
                                                                'the Sages',
                                                                'Mishnah Sheviit 9:9 — the sinner '
                                                                'does not profit; seat: the eaters '
                                                                'and the removal dispute '
                                                                '(LV25A-06), the field-clock '
                                                                '(LV25A-07), the jar dispute '
                                                                '(LV25A-12)')]}},
 'sheviit_release_file': {'tractate': 'Sheviit',
                          'oracle': 'Mishnah Sheviit 10:1; 10:2; 10:3; 10:4; 10:5; 10:6; 10:7; '
                                    "10:8; 10:9 (ROUTED — Deuteronomy 15's span, answered "
                                    "talmud_source-only until the Re'eh walk)",
                          'claim': 'LV25A-13',
                          'anchor': 'Deut.15.1-11 (routed; held at LV25A-13, the two releases '
                                    'matrix) (lev_25_shemittah, LV25A-13)',
                          'cells': {'shemittah_money_release_loans': [('released_written_or_not',
                                                                       None,
                                                                       'Mishnah Sheviit 10:1 — '
                                                                       'releases the loan; seat: '
                                                                       'ROUTED to Deuteronomy 15 — '
                                                                       'held only as the two '
                                                                       'releases matrix (LV25A-13: '
                                                                       'money to the seventh, '
                                                                       'slaves to the Jubilee); '
                                                                       'answered '
                                                                       'talmud_source-only until '
                                                                       "the Re'eh walk")],
                                    'shemittah_shop_credit_wage': [('not_released_unless_made_loan',
                                                                    None,
                                                                    'Mishnah Sheviit 10:1 — shop '
                                                                    'credit is not released; seat: '
                                                                    'ROUTED to Deuteronomy 15 — '
                                                                    'held only as the two releases '
                                                                    'matrix (LV25A-13: money to '
                                                                    'the seventh, slaves to the '
                                                                    'Jubilee); answered '
                                                                    'talmud_source-only until the '
                                                                    "Re'eh walk")],
                                    'shemittah_court_acts_pledge': [('not_released',
                                                                     None,
                                                                     'Mishnah Sheviit 10:2 — and '
                                                                     'every court act is not '
                                                                     'released; seat: ROUTED to '
                                                                     'Deuteronomy 15 — held only '
                                                                     'as the two releases matrix '
                                                                     '(LV25A-13: money to the '
                                                                     'seventh, slaves to the '
                                                                     'Jubilee); answered '
                                                                     'talmud_source-only until the '
                                                                     "Re'eh walk")],
                                    'shemittah_prosbul': [('not_released_hillel_ordinance',
                                                           None,
                                                           'Mishnah Sheviit 10:3 — a prosbul does '
                                                           'not release; seat: ROUTED to '
                                                           'Deuteronomy 15 — held only as the two '
                                                           'releases matrix (LV25A-13: money to '
                                                           'the seventh, slaves to the Jubilee); '
                                                           'answered talmud_source-only until the '
                                                           "Re'eh walk")],
                                    'shemittah_prosbul_text': [('handing_debts_to_judges',
                                                                None,
                                                                'Mishnah Sheviit 10:4 — I hand '
                                                                'over to you; seat: ROUTED to '
                                                                'Deuteronomy 15 — held only as the '
                                                                'two releases matrix (LV25A-13: '
                                                                'money to the seventh, slaves to '
                                                                'the Jubilee); answered '
                                                                'talmud_source-only until the '
                                                                "Re'eh walk")],
                                    'shemittah_prosbul_dating': [('antedated_valid_postdated_invalid',
                                                                  None,
                                                                  'Mishnah Sheviit 10:5 — an '
                                                                  'antedated prosbul is valid; '
                                                                  'seat: ROUTED to Deuteronomy 15 '
                                                                  '— held only as the two releases '
                                                                  'matrix (LV25A-13: money to the '
                                                                  'seventh, slaves to the '
                                                                  'Jubilee); answered '
                                                                  'talmud_source-only until the '
                                                                  "Re'eh walk")],
                                    'shemittah_prosbul_on_land': [('land_required_any_amount',
                                                                   None,
                                                                   'Mishnah Sheviit 10:6 — a '
                                                                   'prosbul is written only on '
                                                                   'land; seat: ROUTED to '
                                                                   'Deuteronomy 15 — held only as '
                                                                   'the two releases matrix '
                                                                   '(LV25A-13: money to the '
                                                                   'seventh, slaves to the '
                                                                   'Jubilee); answered '
                                                                   'talmud_source-only until the '
                                                                   "Re'eh walk")],
                                    'shemittah_beehive_as_land': [('r_eliezer_as_land',
                                                                   'R. Eliezer',
                                                                   'Mishnah Sheviit 10:7 — a '
                                                                   'beehive; seat: ROUTED to '
                                                                   'Deuteronomy 15 — held only as '
                                                                   'the two releases matrix '
                                                                   '(LV25A-13: money to the '
                                                                   'seventh, slaves to the '
                                                                   'Jubilee); answered '
                                                                   'talmud_source-only until the '
                                                                   "Re'eh walk"),
                                                                  ('sages_not_land',
                                                                   'the Sages',
                                                                   'Mishnah Sheviit 10:7 — a '
                                                                   'beehive; seat: ROUTED to '
                                                                   'Deuteronomy 15 — held only as '
                                                                   'the two releases matrix '
                                                                   '(LV25A-13: money to the '
                                                                   'seventh, slaves to the '
                                                                   'Jubilee); answered '
                                                                   'talmud_source-only until the '
                                                                   "Re'eh walk")],
                                    'shemittah_returning_debt_in_seventh': [('say_i_release_then_accept',
                                                                             None,
                                                                             'Mishnah Sheviit 10:8 '
                                                                             '— he says to him: I '
                                                                             'release; seat: '
                                                                             'ROUTED to '
                                                                             'Deuteronomy 15 — '
                                                                             'held only as the two '
                                                                             'releases matrix '
                                                                             '(LV25A-13: money to '
                                                                             'the seventh, slaves '
                                                                             'to the Jubilee); '
                                                                             'answered '
                                                                             'talmud_source-only '
                                                                             "until the Re'eh "
                                                                             'walk')],
                                    'shemittah_sages_pleased': [('spirit_of_sages_pleased',
                                                                 None,
                                                                 'Mishnah Sheviit 10:9 — the '
                                                                 "sages' spirit is pleased with "
                                                                 'him; seat: ROUTED to Deuteronomy '
                                                                 '15 — held only as the two '
                                                                 'releases matrix (LV25A-13: money '
                                                                 'to the seventh, slaves to the '
                                                                 'Jubilee); answered '
                                                                 'talmud_source-only until the '
                                                                 "Re'eh walk")]}},
 'arakhin_supplement_file': {'tractate': 'Arakhin',
                             'oracle': 'Mishnah Arakhin 1:2; 1:3; 2:1; 4:3; 5:1; 5:2; 5:3; 5:4; '
                                       '5:5; 6:1; 6:2; 6:3; 6:4; 6:5; 7:2; 7:3; 7:4; 8:1; 8:2; '
                                       '8:3; 8:4; 9:5; 9:6',
                             'claim': 'LV27-01',
                             'anchor': 'Lev.27.1-25 (with Lev.25.29-30 for 9:5-9:6, '
                                       'lev_25_redeem_poor LV25B-07) (lev_27_vows_valuations, '
                                       'LV27-01, LV27-02, LV27-04, LV27-07, LV27-08, LV27-14, '
                                       'LV27-15, LV27-17, LV27-21, LV25B-07)',
                             'cells': {'arakhin_gentile_valuer_valued': [('r_meir_valued_not_valuer',
                                                                          'R. Meir',
                                                                          'Mishnah Arakhin 1:2 — '
                                                                          'the gentile; seat: the '
                                                                          'valuer/valued split '
                                                                          '(LV27-01), the standing '
                                                                          'predicate (LV27-02), '
                                                                          'limb-sanctification '
                                                                          '(LV27-04), the bidding '
                                                                          'ladder (LV27-07), the '
                                                                          'fifth (LV27-08), son in '
                                                                          'brother out (LV27-14), '
                                                                          'the abandoned field '
                                                                          '(LV27-15), the sela '
                                                                          'floor (LV27-17), the '
                                                                          "condemned's valuation "
                                                                          '(LV27-21); the '
                                                                          'walled-city roster '
                                                                          '(LV25B-07)'),
                                                                         ('r_yehuda_valuer_not_valued',
                                                                          'R. Yehuda',
                                                                          'Mishnah Arakhin 1:2 — '
                                                                          'the gentile; seat: the '
                                                                          'valuer/valued split '
                                                                          '(LV27-01), the standing '
                                                                          'predicate (LV27-02), '
                                                                          'limb-sanctification '
                                                                          '(LV27-04), the bidding '
                                                                          'ladder (LV27-07), the '
                                                                          'fifth (LV27-08), son in '
                                                                          'brother out (LV27-14), '
                                                                          'the abandoned field '
                                                                          '(LV27-15), the sela '
                                                                          'floor (LV27-17), the '
                                                                          "condemned's valuation "
                                                                          '(LV27-21); the '
                                                                          'walled-city roster '
                                                                          '(LV25B-07)')],
                                       'arakhin_dying_and_condemned': [('not_vowed_not_valued',
                                                                        'the first Tanna',
                                                                        'Mishnah Arakhin 1:3 — the '
                                                                        'dying and the one going '
                                                                        'out to be executed; seat: '
                                                                        'the valuer/valued split '
                                                                        '(LV27-01), the standing '
                                                                        'predicate (LV27-02), '
                                                                        'limb-sanctification '
                                                                        '(LV27-04), the bidding '
                                                                        'ladder (LV27-07), the '
                                                                        'fifth (LV27-08), son in '
                                                                        'brother out (LV27-14), '
                                                                        'the abandoned field '
                                                                        '(LV27-15), the sela floor '
                                                                        '(LV27-17), the '
                                                                        "condemned's valuation "
                                                                        '(LV27-21); the '
                                                                        'walled-city roster '
                                                                        '(LV25B-07)'),
                                                                       ('r_chanina_valued_fixed_sum',
                                                                        'R. Chanina b. Akavya',
                                                                        'Mishnah Arakhin 1:3 — the '
                                                                        'dying and the one going '
                                                                        'out to be executed; seat: '
                                                                        'the valuer/valued split '
                                                                        '(LV27-01), the standing '
                                                                        'predicate (LV27-02), '
                                                                        'limb-sanctification '
                                                                        '(LV27-04), the bidding '
                                                                        'ladder (LV27-07), the '
                                                                        'fifth (LV27-08), son in '
                                                                        'brother out (LV27-14), '
                                                                        'the abandoned field '
                                                                        '(LV27-15), the sela floor '
                                                                        '(LV27-17), the '
                                                                        "condemned's valuation "
                                                                        '(LV27-21); the '
                                                                        'walled-city roster '
                                                                        '(LV25B-07)'),
                                                                       ('r_yosei_vows_values_pays',
                                                                        'R. Yosei',
                                                                        'Mishnah Arakhin 1:3 — the '
                                                                        'dying and the one going '
                                                                        'out to be executed; seat: '
                                                                        'the valuer/valued split '
                                                                        '(LV27-01), the standing '
                                                                        'predicate (LV27-02), '
                                                                        'limb-sanctification '
                                                                        '(LV27-04), the bidding '
                                                                        'ladder (LV27-07), the '
                                                                        'fifth (LV27-08), son in '
                                                                        'brother out (LV27-14), '
                                                                        'the abandoned field '
                                                                        '(LV27-15), the sela floor '
                                                                        '(LV27-17), the '
                                                                        "condemned's valuation "
                                                                        '(LV27-21); the '
                                                                        'walled-city roster '
                                                                        '(LV25B-07)')],
                                       'arakhin_floor_ceiling': [('sela_to_fifty',
                                                                  None,
                                                                  'Mishnah Arakhin 2:1 — no '
                                                                  'valuation under a sela; seat: '
                                                                  'the valuer/valued split '
                                                                  '(LV27-01), the standing '
                                                                  'predicate (LV27-02), '
                                                                  'limb-sanctification (LV27-04), '
                                                                  'the bidding ladder (LV27-07), '
                                                                  'the fifth (LV27-08), son in '
                                                                  'brother out (LV27-14), the '
                                                                  'abandoned field (LV27-15), the '
                                                                  'sela floor (LV27-17), the '
                                                                  "condemned's valuation "
                                                                  '(LV27-21); the walled-city '
                                                                  'roster (LV25B-07)')],
                                       'arakhin_five_selas_in_hand': [('r_meir_one',
                                                                       'R. Meir',
                                                                       'Mishnah Arakhin 2:1 — he '
                                                                       'had five selas in hand; '
                                                                       'seat: the valuer/valued '
                                                                       'split (LV27-01), the '
                                                                       'standing predicate '
                                                                       '(LV27-02), '
                                                                       'limb-sanctification '
                                                                       '(LV27-04), the bidding '
                                                                       'ladder (LV27-07), the '
                                                                       'fifth (LV27-08), son in '
                                                                       'brother out (LV27-14), the '
                                                                       'abandoned field (LV27-15), '
                                                                       'the sela floor (LV27-17), '
                                                                       "the condemned's valuation "
                                                                       '(LV27-21); the walled-city '
                                                                       'roster (LV25B-07)'),
                                                                      ('sages_all',
                                                                       'the Sages',
                                                                       'Mishnah Arakhin 2:1 — he '
                                                                       'had five selas in hand; '
                                                                       'seat: the valuer/valued '
                                                                       'split (LV27-01), the '
                                                                       'standing predicate '
                                                                       '(LV27-02), '
                                                                       'limb-sanctification '
                                                                       '(LV27-04), the bidding '
                                                                       'ladder (LV27-07), the '
                                                                       'fifth (LV27-08), son in '
                                                                       'brother out (LV27-14), the '
                                                                       'abandoned field (LV27-15), '
                                                                       'the sela floor (LV27-17), '
                                                                       "the condemned's valuation "
                                                                       '(LV27-21); the walled-city '
                                                                       'roster (LV25B-07)')],
                                       'arakhin_offering_means_windfall': [('sanctuary_has_nothing',
                                                                            None,
                                                                            'Mishnah Arakhin 4:3 — '
                                                                            'the sanctuary has '
                                                                            'nothing of them; '
                                                                            'seat: the '
                                                                            'valuer/valued split '
                                                                            '(LV27-01), the '
                                                                            'standing predicate '
                                                                            '(LV27-02), '
                                                                            'limb-sanctification '
                                                                            '(LV27-04), the '
                                                                            'bidding ladder '
                                                                            '(LV27-07), the fifth '
                                                                            '(LV27-08), son in '
                                                                            'brother out '
                                                                            '(LV27-14), the '
                                                                            'abandoned field '
                                                                            '(LV27-15), the sela '
                                                                            'floor (LV27-17), the '
                                                                            "condemned's valuation "
                                                                            '(LV27-21); the '
                                                                            'walled-city roster '
                                                                            '(LV25B-07)')],
                                       'arakhin_my_weight_upon_me': [('gives_his_weight_as_said',
                                                                      None,
                                                                      'Mishnah Arakhin 5:1 — my '
                                                                      'weight upon me; seat: the '
                                                                      'valuer/valued split '
                                                                      '(LV27-01), the standing '
                                                                      'predicate (LV27-02), '
                                                                      'limb-sanctification '
                                                                      '(LV27-04), the bidding '
                                                                      'ladder (LV27-07), the fifth '
                                                                      '(LV27-08), son in brother '
                                                                      'out (LV27-14), the '
                                                                      'abandoned field (LV27-15), '
                                                                      'the sela floor (LV27-17), '
                                                                      "the condemned's valuation "
                                                                      '(LV27-21); the walled-city '
                                                                      'roster (LV25B-07)')],
                                       'arakhin_hand_weight': [('r_yehuda_barrel',
                                                                'R. Yehuda',
                                                                "Mishnah Arakhin 5:1 — my hand's "
                                                                'weight upon me; seat: the '
                                                                'valuer/valued split (LV27-01), '
                                                                'the standing predicate (LV27-02), '
                                                                'limb-sanctification (LV27-04), '
                                                                'the bidding ladder (LV27-07), the '
                                                                'fifth (LV27-08), son in brother '
                                                                'out (LV27-14), the abandoned '
                                                                'field (LV27-15), the sela floor '
                                                                "(LV27-17), the condemned's "
                                                                'valuation (LV27-21); the '
                                                                'walled-city roster (LV25B-07)'),
                                                               ('r_yosei_assess',
                                                                'R. Yosei',
                                                                "Mishnah Arakhin 5:1 — my hand's "
                                                                'weight upon me; seat: the '
                                                                'valuer/valued split (LV27-01), '
                                                                'the standing predicate (LV27-02), '
                                                                'limb-sanctification (LV27-04), '
                                                                'the bidding ladder (LV27-07), the '
                                                                'fifth (LV27-08), son in brother '
                                                                'out (LV27-14), the abandoned '
                                                                'field (LV27-15), the sela floor '
                                                                "(LV27-17), the condemned's "
                                                                'valuation (LV27-21); the '
                                                                'walled-city roster (LV25B-07)')],
                                       'arakhin_limb_soul_depends': [('gives_whole_valuation',
                                                                      None,
                                                                      'Mishnah Arakhin 5:2 — a '
                                                                      'thing the soul depends on; '
                                                                      'seat: the valuer/valued '
                                                                      'split (LV27-01), the '
                                                                      'standing predicate '
                                                                      '(LV27-02), '
                                                                      'limb-sanctification '
                                                                      '(LV27-04), the bidding '
                                                                      'ladder (LV27-07), the fifth '
                                                                      '(LV27-08), son in brother '
                                                                      'out (LV27-14), the '
                                                                      'abandoned field (LV27-15), '
                                                                      'the sela floor (LV27-17), '
                                                                      "the condemned's valuation "
                                                                      '(LV27-21); the walled-city '
                                                                      'roster (LV25B-07)')],
                                       'arakhin_worth_of_dead': [('none_valuation_heirs_pay',
                                                                  None,
                                                                  'Mishnah Arakhin 5:2 — for the '
                                                                  'dead have no worth; seat: the '
                                                                  'valuer/valued split (LV27-01), '
                                                                  'the standing predicate '
                                                                  '(LV27-02), limb-sanctification '
                                                                  '(LV27-04), the bidding ladder '
                                                                  '(LV27-07), the fifth (LV27-08), '
                                                                  'son in brother out (LV27-14), '
                                                                  'the abandoned field (LV27-15), '
                                                                  'the sela floor (LV27-17), the '
                                                                  "condemned's valuation "
                                                                  '(LV27-21); the walled-city '
                                                                  'roster (LV25B-07)')],
                                       'arakhin_half_valuation_vs_valuation_of_half': [('half_vs_whole',
                                                                                        None,
                                                                                        'Mishnah '
                                                                                        'Arakhin '
                                                                                        '5:3 — '
                                                                                        'half my '
                                                                                        'valuation '
                                                                                        'upon me; '
                                                                                        'seat: the '
                                                                                        'valuer/valued '
                                                                                        'split '
                                                                                        '(LV27-01), '
                                                                                        'the '
                                                                                        'standing '
                                                                                        'predicate '
                                                                                        '(LV27-02), '
                                                                                        'limb-sanctification '
                                                                                        '(LV27-04), '
                                                                                        'the '
                                                                                        'bidding '
                                                                                        'ladder '
                                                                                        '(LV27-07), '
                                                                                        'the fifth '
                                                                                        '(LV27-08), '
                                                                                        'son in '
                                                                                        'brother '
                                                                                        'out '
                                                                                        '(LV27-14), '
                                                                                        'the '
                                                                                        'abandoned '
                                                                                        'field '
                                                                                        '(LV27-15), '
                                                                                        'the sela '
                                                                                        'floor '
                                                                                        '(LV27-17), '
                                                                                        'the '
                                                                                        "condemned's "
                                                                                        'valuation '
                                                                                        '(LV27-21); '
                                                                                        'the '
                                                                                        'walled-city '
                                                                                        'roster '
                                                                                        '(LV25B-07)')],
                                       'arakhin_vower_or_valued_died': [('valuation_heirs_pay_worth_not_for_dead',
                                                                         None,
                                                                         'Mishnah Arakhin 5:4 — '
                                                                         'the vower and the valued '
                                                                         'died — the heirs pay; '
                                                                         'seat: the valuer/valued '
                                                                         'split (LV27-01), the '
                                                                         'standing predicate '
                                                                         '(LV27-02), '
                                                                         'limb-sanctification '
                                                                         '(LV27-04), the bidding '
                                                                         'ladder (LV27-07), the '
                                                                         'fifth (LV27-08), son in '
                                                                         'brother out (LV27-14), '
                                                                         'the abandoned field '
                                                                         '(LV27-15), the sela '
                                                                         'floor (LV27-17), the '
                                                                         "condemned's valuation "
                                                                         '(LV27-21); the '
                                                                         'walled-city roster '
                                                                         '(LV25B-07)')],
                                       'arakhin_object_vow_vs_sum_vow': [('object_dies_exempt_sum_liable',
                                                                          None,
                                                                          'Mishnah Arakhin 5:5 — '
                                                                          'this ox is an olah; '
                                                                          'seat: the valuer/valued '
                                                                          'split (LV27-01), the '
                                                                          'standing predicate '
                                                                          '(LV27-02), '
                                                                          'limb-sanctification '
                                                                          '(LV27-04), the bidding '
                                                                          'ladder (LV27-07), the '
                                                                          'fifth (LV27-08), son in '
                                                                          'brother out (LV27-14), '
                                                                          'the abandoned field '
                                                                          '(LV27-15), the sela '
                                                                          'floor (LV27-17), the '
                                                                          "condemned's valuation "
                                                                          '(LV27-21); the '
                                                                          'walled-city roster '
                                                                          '(LV25B-07)')],
                                       'arakhin_assessment_days': [('orphans_thirty_sanctuary_sixty',
                                                                    None,
                                                                    'Mishnah Arakhin 6:1 — the '
                                                                    "orphans' assessment thirty "
                                                                    'days; seat: the valuer/valued '
                                                                    'split (LV27-01), the standing '
                                                                    'predicate (LV27-02), '
                                                                    'limb-sanctification '
                                                                    '(LV27-04), the bidding ladder '
                                                                    '(LV27-07), the fifth '
                                                                    '(LV27-08), son in brother out '
                                                                    '(LV27-14), the abandoned '
                                                                    'field (LV27-15), the sela '
                                                                    'floor (LV27-17), the '
                                                                    "condemned's valuation "
                                                                    '(LV27-21); the walled-city '
                                                                    'roster (LV25B-07)')],
                                       'arakhin_consecrated_with_ketubah_creditor': [('redeem_on_condition_add_dinar',
                                                                                      None,
                                                                                      'Mishnah '
                                                                                      'Arakhin 6:2 '
                                                                                      '— he adds a '
                                                                                      'dinar and '
                                                                                      'redeems; '
                                                                                      'seat: the '
                                                                                      'valuer/valued '
                                                                                      'split '
                                                                                      '(LV27-01), '
                                                                                      'the '
                                                                                      'standing '
                                                                                      'predicate '
                                                                                      '(LV27-02), '
                                                                                      'limb-sanctification '
                                                                                      '(LV27-04), '
                                                                                      'the bidding '
                                                                                      'ladder '
                                                                                      '(LV27-07), '
                                                                                      'the fifth '
                                                                                      '(LV27-08), '
                                                                                      'son in '
                                                                                      'brother out '
                                                                                      '(LV27-14), '
                                                                                      'the '
                                                                                      'abandoned '
                                                                                      'field '
                                                                                      '(LV27-15), '
                                                                                      'the sela '
                                                                                      'floor '
                                                                                      '(LV27-17), '
                                                                                      'the '
                                                                                      "condemned's "
                                                                                      'valuation '
                                                                                      '(LV27-21); '
                                                                                      'the '
                                                                                      'walled-city '
                                                                                      'roster '
                                                                                      '(LV25B-07)')],
                                       'arakhin_seizure_leaves': [('thirty_days_food_twelve_months_clothing',
                                                                   None,
                                                                   'Mishnah Arakhin 6:3 — they '
                                                                   "leave him thirty days' food; "
                                                                   'seat: the valuer/valued split '
                                                                   '(LV27-01), the standing '
                                                                   'predicate (LV27-02), '
                                                                   'limb-sanctification (LV27-04), '
                                                                   'the bidding ladder (LV27-07), '
                                                                   'the fifth (LV27-08), son in '
                                                                   'brother out (LV27-14), the '
                                                                   'abandoned field (LV27-15), the '
                                                                   'sela floor (LV27-17), the '
                                                                   "condemned's valuation "
                                                                   '(LV27-21); the walled-city '
                                                                   'roster (LV25B-07)')],
                                       'arakhin_craftsman_tools_left': [('two_of_each_kind',
                                                                         None,
                                                                         'Mishnah Arakhin 6:3 — '
                                                                         'two tools of each kind; '
                                                                         'seat: the valuer/valued '
                                                                         'split (LV27-01), the '
                                                                         'standing predicate '
                                                                         '(LV27-02), '
                                                                         'limb-sanctification '
                                                                         '(LV27-04), the bidding '
                                                                         'ladder (LV27-07), the '
                                                                         'fifth (LV27-08), son in '
                                                                         'brother out (LV27-14), '
                                                                         'the abandoned field '
                                                                         '(LV27-15), the sela '
                                                                         'floor (LV27-17), the '
                                                                         "condemned's valuation "
                                                                         '(LV27-21); the '
                                                                         'walled-city roster '
                                                                         '(LV25B-07)')],
                                       'arakhin_many_of_one_kind_few_of_another': [('two_of_many_all_of_few',
                                                                                    None,
                                                                                    'Mishnah '
                                                                                    'Arakhin 6:4 — '
                                                                                    'they give him '
                                                                                    'two of the '
                                                                                    'many kind; '
                                                                                    'seat: the '
                                                                                    'valuer/valued '
                                                                                    'split '
                                                                                    '(LV27-01), '
                                                                                    'the standing '
                                                                                    'predicate '
                                                                                    '(LV27-02), '
                                                                                    'limb-sanctification '
                                                                                    '(LV27-04), '
                                                                                    'the bidding '
                                                                                    'ladder '
                                                                                    '(LV27-07), '
                                                                                    'the fifth '
                                                                                    '(LV27-08), '
                                                                                    'son in '
                                                                                    'brother out '
                                                                                    '(LV27-14), '
                                                                                    'the abandoned '
                                                                                    'field '
                                                                                    '(LV27-15), '
                                                                                    'the sela '
                                                                                    'floor '
                                                                                    '(LV27-17), '
                                                                                    'the '
                                                                                    "condemned's "
                                                                                    'valuation '
                                                                                    '(LV27-21); '
                                                                                    'the '
                                                                                    'walled-city '
                                                                                    'roster '
                                                                                    '(LV25B-07)')],
                                       'arakhin_sanctuary_place_and_hour': [('assessed_at_spot',
                                                                             None,
                                                                             'Mishnah Arakhin 6:5 '
                                                                             '— the sanctuary has '
                                                                             'only its place and '
                                                                             'its hour; seat: the '
                                                                             'valuer/valued split '
                                                                             '(LV27-01), the '
                                                                             'standing predicate '
                                                                             '(LV27-02), '
                                                                             'limb-sanctification '
                                                                             '(LV27-04), the '
                                                                             'bidding ladder '
                                                                             '(LV27-07), the fifth '
                                                                             '(LV27-08), son in '
                                                                             'brother out '
                                                                             '(LV27-14), the '
                                                                             'abandoned field '
                                                                             '(LV27-15), the sela '
                                                                             'floor (LV27-17), the '
                                                                             "condemned's "
                                                                             'valuation (LV27-21); '
                                                                             'the walled-city '
                                                                             'roster (LV25B-07)')],
                                       'arakhin_fifth_owner_only': [('owner_adds_fifth',
                                                                     None,
                                                                     'Mishnah Arakhin 7:2 — the '
                                                                     'owner gives a fifth; seat: '
                                                                     'the valuer/valued split '
                                                                     '(LV27-01), the standing '
                                                                     'predicate (LV27-02), '
                                                                     'limb-sanctification '
                                                                     '(LV27-04), the bidding '
                                                                     'ladder (LV27-07), the fifth '
                                                                     '(LV27-08), son in brother '
                                                                     'out (LV27-14), the abandoned '
                                                                     'field (LV27-15), the sela '
                                                                     'floor (LV27-17), the '
                                                                     "condemned's valuation "
                                                                     '(LV27-21); the walled-city '
                                                                     'roster (LV25B-07)')],
                                       'arakhin_field_redeemed_by_son': [('returns_to_father_at_jubilee',
                                                                          None,
                                                                          'Mishnah Arakhin 7:3 — '
                                                                          'his son redeemed it — '
                                                                          'it leaves to the father '
                                                                          'at the Jubilee; seat: '
                                                                          'the valuer/valued split '
                                                                          '(LV27-01), the standing '
                                                                          'predicate (LV27-02), '
                                                                          'limb-sanctification '
                                                                          '(LV27-04), the bidding '
                                                                          'ladder (LV27-07), the '
                                                                          'fifth (LV27-08), son in '
                                                                          'brother out (LV27-14), '
                                                                          'the abandoned field '
                                                                          '(LV27-15), the sela '
                                                                          'floor (LV27-17), the '
                                                                          "condemned's valuation "
                                                                          '(LV27-21); the '
                                                                          'walled-city roster '
                                                                          '(LV25B-07)')],
                                       'arakhin_field_redeemed_by_priest': [('to_all_brother_priests',
                                                                             None,
                                                                             'Mishnah Arakhin 7:3 '
                                                                             '— it leaves to all '
                                                                             'his brother priests; '
                                                                             'seat: the '
                                                                             'valuer/valued split '
                                                                             '(LV27-01), the '
                                                                             'standing predicate '
                                                                             '(LV27-02), '
                                                                             'limb-sanctification '
                                                                             '(LV27-04), the '
                                                                             'bidding ladder '
                                                                             '(LV27-07), the fifth '
                                                                             '(LV27-08), son in '
                                                                             'brother out '
                                                                             '(LV27-14), the '
                                                                             'abandoned field '
                                                                             '(LV27-15), the sela '
                                                                             'floor (LV27-17), the '
                                                                             "condemned's "
                                                                             'valuation (LV27-21); '
                                                                             'the walled-city '
                                                                             'roster (LV25B-07)')],
                                       'arakhin_jubilee_unredeemed_field': [('r_yehuda_enter_and_pay',
                                                                             'R. Yehuda',
                                                                             'Mishnah Arakhin 7:4 '
                                                                             '— it is called the '
                                                                             'abandoned field; '
                                                                             'seat: the '
                                                                             'valuer/valued split '
                                                                             '(LV27-01), the '
                                                                             'standing predicate '
                                                                             '(LV27-02), '
                                                                             'limb-sanctification '
                                                                             '(LV27-04), the '
                                                                             'bidding ladder '
                                                                             '(LV27-07), the fifth '
                                                                             '(LV27-08), son in '
                                                                             'brother out '
                                                                             '(LV27-14), the '
                                                                             'abandoned field '
                                                                             '(LV27-15), the sela '
                                                                             'floor (LV27-17), the '
                                                                             "condemned's "
                                                                             'valuation (LV27-21); '
                                                                             'the walled-city '
                                                                             'roster (LV25B-07)'),
                                                                            ('r_shimon_enter_not_pay',
                                                                             'R. Shimon',
                                                                             'Mishnah Arakhin 7:4 '
                                                                             '— it is called the '
                                                                             'abandoned field; '
                                                                             'seat: the '
                                                                             'valuer/valued split '
                                                                             '(LV27-01), the '
                                                                             'standing predicate '
                                                                             '(LV27-02), '
                                                                             'limb-sanctification '
                                                                             '(LV27-04), the '
                                                                             'bidding ladder '
                                                                             '(LV27-07), the fifth '
                                                                             '(LV27-08), son in '
                                                                             'brother out '
                                                                             '(LV27-14), the '
                                                                             'abandoned field '
                                                                             '(LV27-15), the sela '
                                                                             'floor (LV27-17), the '
                                                                             "condemned's "
                                                                             'valuation (LV27-21); '
                                                                             'the walled-city '
                                                                             'roster (LV25B-07)'),
                                                                            ('r_eliezer_abandoned_field',
                                                                             'R. Eliezer',
                                                                             'Mishnah Arakhin 7:4 '
                                                                             '— it is called the '
                                                                             'abandoned field; '
                                                                             'seat: the '
                                                                             'valuer/valued split '
                                                                             '(LV27-01), the '
                                                                             'standing predicate '
                                                                             '(LV27-02), '
                                                                             'limb-sanctification '
                                                                             '(LV27-04), the '
                                                                             'bidding ladder '
                                                                             '(LV27-07), the fifth '
                                                                             '(LV27-08), son in '
                                                                             'brother out '
                                                                             '(LV27-14), the '
                                                                             'abandoned field '
                                                                             '(LV27-15), the sela '
                                                                             'floor (LV27-17), the '
                                                                             "condemned's "
                                                                             'valuation (LV27-21); '
                                                                             'the walled-city '
                                                                             'roster (LV25B-07)')],
                                       'arakhin_owner_opens_first': [('owner_first_adds_fifth',
                                                                      None,
                                                                      'Mishnah Arakhin 8:1 — you '
                                                                      'open first; seat: the '
                                                                      'valuer/valued split '
                                                                      '(LV27-01), the standing '
                                                                      'predicate (LV27-02), '
                                                                      'limb-sanctification '
                                                                      '(LV27-04), the bidding '
                                                                      'ladder (LV27-07), the fifth '
                                                                      '(LV27-08), son in brother '
                                                                      'out (LV27-14), the '
                                                                      'abandoned field (LV27-15), '
                                                                      'the sela floor (LV27-17), '
                                                                      "the condemned's valuation "
                                                                      '(LV27-21); the walled-city '
                                                                      'roster (LV25B-07)')],
                                       'arakhin_bid_of_an_issar': [('it_is_yours_loses_issar',
                                                                    'the first Tanna',
                                                                    'Mishnah Arakhin 8:1 — it is '
                                                                    'mine for an issar; seat: the '
                                                                    'valuer/valued split '
                                                                    '(LV27-01), the standing '
                                                                    'predicate (LV27-02), '
                                                                    'limb-sanctification '
                                                                    '(LV27-04), the bidding ladder '
                                                                    '(LV27-07), the fifth '
                                                                    '(LV27-08), son in brother out '
                                                                    '(LV27-14), the abandoned '
                                                                    'field (LV27-15), the sela '
                                                                    'floor (LV27-17), the '
                                                                    "condemned's valuation "
                                                                    '(LV27-21); the walled-city '
                                                                    'roster (LV25B-07)'),
                                                                   ('r_yosei_egg_worth',
                                                                    'R. Yosei',
                                                                    'Mishnah Arakhin 8:1 — it is '
                                                                    'mine for an issar; seat: the '
                                                                    'valuer/valued split '
                                                                    '(LV27-01), the standing '
                                                                    'predicate (LV27-02), '
                                                                    'limb-sanctification '
                                                                    '(LV27-04), the bidding ladder '
                                                                    '(LV27-07), the fifth '
                                                                    '(LV27-08), son in brother out '
                                                                    '(LV27-14), the abandoned '
                                                                    'field (LV27-15), the sela '
                                                                    'floor (LV27-17), the '
                                                                    "condemned's valuation "
                                                                    '(LV27-21); the walled-city '
                                                                    'roster (LV25B-07)')],
                                       'arakhin_bidder_retracts': [('seized_to_ten',
                                                                    None,
                                                                    'Mishnah Arakhin 8:2 — his '
                                                                    'property seized to ten; seat: '
                                                                    'the valuer/valued split '
                                                                    '(LV27-01), the standing '
                                                                    'predicate (LV27-02), '
                                                                    'limb-sanctification '
                                                                    '(LV27-04), the bidding ladder '
                                                                    '(LV27-07), the fifth '
                                                                    '(LV27-08), son in brother out '
                                                                    '(LV27-14), the abandoned '
                                                                    'field (LV27-15), the sela '
                                                                    'floor (LV27-17), the '
                                                                    "condemned's valuation "
                                                                    '(LV27-21); the walled-city '
                                                                    'roster (LV25B-07)')],
                                       'arakhin_owner_and_all_at_twenty': [('owner_first',
                                                                            None,
                                                                            'Mishnah Arakhin 8:2 — '
                                                                            'the owners come '
                                                                            'first; seat: the '
                                                                            'valuer/valued split '
                                                                            '(LV27-01), the '
                                                                            'standing predicate '
                                                                            '(LV27-02), '
                                                                            'limb-sanctification '
                                                                            '(LV27-04), the '
                                                                            'bidding ladder '
                                                                            '(LV27-07), the fifth '
                                                                            '(LV27-08), son in '
                                                                            'brother out '
                                                                            '(LV27-14), the '
                                                                            'abandoned field '
                                                                            '(LV27-15), the sela '
                                                                            'floor (LV27-17), the '
                                                                            "condemned's valuation "
                                                                            '(LV27-21); the '
                                                                            'walled-city roster '
                                                                            '(LV25B-07)')],
                                       'arakhin_fifth_arithmetic_twenty_five': [('thirty',
                                                                                 None,
                                                                                 'Mishnah Arakhin '
                                                                                 '8:3 — at '
                                                                                 'twenty-five the '
                                                                                 'owners give '
                                                                                 'thirty; seat: '
                                                                                 'the '
                                                                                 'valuer/valued '
                                                                                 'split (LV27-01), '
                                                                                 'the standing '
                                                                                 'predicate '
                                                                                 '(LV27-02), '
                                                                                 'limb-sanctification '
                                                                                 '(LV27-04), the '
                                                                                 'bidding ladder '
                                                                                 '(LV27-07), the '
                                                                                 'fifth (LV27-08), '
                                                                                 'son in brother '
                                                                                 'out (LV27-14), '
                                                                                 'the abandoned '
                                                                                 'field (LV27-15), '
                                                                                 'the sela floor '
                                                                                 '(LV27-17), the '
                                                                                 "condemned's "
                                                                                 'valuation '
                                                                                 '(LV27-21); the '
                                                                                 'walled-city '
                                                                                 'roster '
                                                                                 '(LV25B-07)')],
                                       'arakhin_fifth_arithmetic_twenty_six': [('thirty_one_and_a_dinar',
                                                                                None,
                                                                                'Mishnah Arakhin '
                                                                                '8:3 — thirty-one '
                                                                                'and a dinar; '
                                                                                'seat: the '
                                                                                'valuer/valued '
                                                                                'split (LV27-01), '
                                                                                'the standing '
                                                                                'predicate '
                                                                                '(LV27-02), '
                                                                                'limb-sanctification '
                                                                                '(LV27-04), the '
                                                                                'bidding ladder '
                                                                                '(LV27-07), the '
                                                                                'fifth (LV27-08), '
                                                                                'son in brother '
                                                                                'out (LV27-14), '
                                                                                'the abandoned '
                                                                                'field (LV27-15), '
                                                                                'the sela floor '
                                                                                '(LV27-17), the '
                                                                                "condemned's "
                                                                                'valuation '
                                                                                '(LV27-21); the '
                                                                                'walled-city '
                                                                                'roster '
                                                                                '(LV25B-07)')],
                                       'arakhin_devoting_all_property': [('r_elazar_not_devoted',
                                                                          'R. Elazar',
                                                                          'Mishnah Arakhin 8:4 — '
                                                                          'and if he devoted all '
                                                                          'of them; seat: the '
                                                                          'valuer/valued split '
                                                                          '(LV27-01), the standing '
                                                                          'predicate (LV27-02), '
                                                                          'limb-sanctification '
                                                                          '(LV27-04), the bidding '
                                                                          'ladder (LV27-07), the '
                                                                          'fifth (LV27-08), son in '
                                                                          'brother out (LV27-14), '
                                                                          'the abandoned field '
                                                                          '(LV27-15), the sela '
                                                                          'floor (LV27-17), the '
                                                                          "condemned's valuation "
                                                                          '(LV27-21); the '
                                                                          'walled-city roster '
                                                                          '(LV25B-07)'),
                                                                         ('r_elazar_b_azaryah_spare',
                                                                          'R. Elazar b. Azaryah',
                                                                          'Mishnah Arakhin 8:4 — '
                                                                          'and if he devoted all '
                                                                          'of them; seat: the '
                                                                          'valuer/valued split '
                                                                          '(LV27-01), the standing '
                                                                          'predicate (LV27-02), '
                                                                          'limb-sanctification '
                                                                          '(LV27-04), the bidding '
                                                                          'ladder (LV27-07), the '
                                                                          'fifth (LV27-08), son in '
                                                                          'brother out (LV27-14), '
                                                                          'the abandoned field '
                                                                          '(LV27-15), the sela '
                                                                          'floor (LV27-17), the '
                                                                          "condemned's valuation "
                                                                          '(LV27-21); the '
                                                                          'walled-city roster '
                                                                          '(LV25B-07)')],
                                       'arakhin_within_wall_fields': [('fields_excluded',
                                                                       'the first Tanna',
                                                                       'Mishnah Arakhin 9:5 — '
                                                                       'except the fields; seat: '
                                                                       'the valuer/valued split '
                                                                       '(LV27-01), the standing '
                                                                       'predicate (LV27-02), '
                                                                       'limb-sanctification '
                                                                       '(LV27-04), the bidding '
                                                                       'ladder (LV27-07), the '
                                                                       'fifth (LV27-08), son in '
                                                                       'brother out (LV27-14), the '
                                                                       'abandoned field (LV27-15), '
                                                                       'the sela floor (LV27-17), '
                                                                       "the condemned's valuation "
                                                                       '(LV27-21); the walled-city '
                                                                       'roster (LV25B-07)'),
                                                                      ('r_meir_even_fields',
                                                                       'R. Meir',
                                                                       'Mishnah Arakhin 9:5 — '
                                                                       'except the fields; seat: '
                                                                       'the valuer/valued split '
                                                                       '(LV27-01), the standing '
                                                                       'predicate (LV27-02), '
                                                                       'limb-sanctification '
                                                                       '(LV27-04), the bidding '
                                                                       'ladder (LV27-07), the '
                                                                       'fifth (LV27-08), son in '
                                                                       'brother out (LV27-14), the '
                                                                       'abandoned field (LV27-15), '
                                                                       'the sela floor (LV27-17), '
                                                                       "the condemned's valuation "
                                                                       '(LV27-21); the walled-city '
                                                                       'roster (LV25B-07)')],
                                       'arakhin_house_built_in_wall': [('r_yehuda_not_walled',
                                                                        'R. Yehuda',
                                                                        'Mishnah Arakhin 9:5 — a '
                                                                        'house built in the wall; '
                                                                        'seat: the valuer/valued '
                                                                        'split (LV27-01), the '
                                                                        'standing predicate '
                                                                        '(LV27-02), '
                                                                        'limb-sanctification '
                                                                        '(LV27-04), the bidding '
                                                                        'ladder (LV27-07), the '
                                                                        'fifth (LV27-08), son in '
                                                                        'brother out (LV27-14), '
                                                                        'the abandoned field '
                                                                        '(LV27-15), the sela floor '
                                                                        '(LV27-17), the '
                                                                        "condemned's valuation "
                                                                        '(LV27-21); the '
                                                                        'walled-city roster '
                                                                        '(LV25B-07)'),
                                                                       ('r_shimon_outer_wall_is_wall',
                                                                        'R. Shimon',
                                                                        'Mishnah Arakhin 9:5 — a '
                                                                        'house built in the wall; '
                                                                        'seat: the valuer/valued '
                                                                        'split (LV27-01), the '
                                                                        'standing predicate '
                                                                        '(LV27-02), '
                                                                        'limb-sanctification '
                                                                        '(LV27-04), the bidding '
                                                                        'ladder (LV27-07), the '
                                                                        'fifth (LV27-08), son in '
                                                                        'brother out (LV27-14), '
                                                                        'the abandoned field '
                                                                        '(LV27-15), the sela floor '
                                                                        '(LV27-17), the '
                                                                        "condemned's valuation "
                                                                        '(LV27-21); the '
                                                                        'walled-city roster '
                                                                        '(LV25B-07)')],
                                       'arakhin_walled_city_roster': [('since_joshua_three_courtyards',
                                                                       None,
                                                                       'Mishnah Arakhin 9:6 — '
                                                                       'walled since the days of '
                                                                       'Joshua son of Nun; seat: '
                                                                       'the valuer/valued split '
                                                                       '(LV27-01), the standing '
                                                                       'predicate (LV27-02), '
                                                                       'limb-sanctification '
                                                                       '(LV27-04), the bidding '
                                                                       'ladder (LV27-07), the '
                                                                       'fifth (LV27-08), son in '
                                                                       'brother out (LV27-14), the '
                                                                       'abandoned field (LV27-15), '
                                                                       'the sela floor (LV27-17), '
                                                                       "the condemned's valuation "
                                                                       '(LV27-21); the walled-city '
                                                                       'roster (LV25B-07)')]}},
 'temurah_supplement_file': {'tractate': 'Temurah',
                             'oracle': 'Mishnah Temurah 1:3; 1:5; 2:1; 2:3; 3:1; 3:3; 3:5; 5:1; '
                                       '5:2; 5:3; 5:4; 5:5; 5:6; 7:1; 7:2; 7:3',
                             'claim': 'LV27-05',
                             'anchor': 'Lev.27.9-15 and 27:26-33 (lev_27_vows_valuations, LV27-04, '
                                       'LV27-05, LV27-06, LV27-09, LV27-18, LV27-22)',
                             'cells': {'temurah_limbs_embryos': [('not_substituted',
                                                                  'the first Tanna',
                                                                  'Mishnah Temurah 1:3 — no '
                                                                  'substituting limbs for embryos; '
                                                                  'seat: limb-sanctification and '
                                                                  'individuals only (LV27-04), '
                                                                  'substitution not transitive '
                                                                  '(LV27-05), disqualified '
                                                                  'consecrated beasts (LV27-06), '
                                                                  'unspecified to upkeep '
                                                                  '(LV27-09), outwitting the '
                                                                  'firstborn (LV27-18), the '
                                                                  "tithe's domain (LV27-22)"),
                                                                 ('r_yosei_limbs_for_whole',
                                                                  'R. Yosei',
                                                                  'Mishnah Temurah 1:3 — no '
                                                                  'substituting limbs for embryos; '
                                                                  'seat: limb-sanctification and '
                                                                  'individuals only (LV27-04), '
                                                                  'substitution not transitive '
                                                                  '(LV27-05), disqualified '
                                                                  'consecrated beasts (LV27-06), '
                                                                  'unspecified to upkeep '
                                                                  '(LV27-09), outwitting the '
                                                                  'firstborn (LV27-18), the '
                                                                  "tithe's domain (LV27-22)")],
                                       'temurah_substitute_makes_substitute': [('no',
                                                                                'the Sages',
                                                                                'Mishnah Temurah '
                                                                                '1:5 — and no '
                                                                                'substitute makes '
                                                                                'a substitute; '
                                                                                'seat: '
                                                                                'limb-sanctification '
                                                                                'and individuals '
                                                                                'only (LV27-04), '
                                                                                'substitution not '
                                                                                'transitive '
                                                                                '(LV27-05), '
                                                                                'disqualified '
                                                                                'consecrated '
                                                                                'beasts (LV27-06), '
                                                                                'unspecified to '
                                                                                'upkeep (LV27-09), '
                                                                                'outwitting the '
                                                                                'firstborn '
                                                                                '(LV27-18), the '
                                                                                "tithe's domain "
                                                                                '(LV27-22)'),
                                                                               ('r_yehuda_offspring_does',
                                                                                'R. Yehuda',
                                                                                'Mishnah Temurah '
                                                                                '1:5 — and no '
                                                                                'substitute makes '
                                                                                'a substitute; '
                                                                                'seat: '
                                                                                'limb-sanctification '
                                                                                'and individuals '
                                                                                'only (LV27-04), '
                                                                                'substitution not '
                                                                                'transitive '
                                                                                '(LV27-05), '
                                                                                'disqualified '
                                                                                'consecrated '
                                                                                'beasts (LV27-06), '
                                                                                'unspecified to '
                                                                                'upkeep (LV27-09), '
                                                                                'outwitting the '
                                                                                'firstborn '
                                                                                '(LV27-18), the '
                                                                                "tithe's domain "
                                                                                '(LV27-22)')],
                                       'temurah_community_offerings': [('do_not_substitute',
                                                                        None,
                                                                        'Mishnah Temurah 2:1 — and '
                                                                        "the community's offerings "
                                                                        'make no substitute; seat: '
                                                                        'limb-sanctification and '
                                                                        'individuals only '
                                                                        '(LV27-04), substitution '
                                                                        'not transitive (LV27-05), '
                                                                        'disqualified consecrated '
                                                                        'beasts (LV27-06), '
                                                                        'unspecified to upkeep '
                                                                        '(LV27-09), outwitting the '
                                                                        'firstborn (LV27-18), the '
                                                                        "tithe's domain "
                                                                        '(LV27-22)')],
                                       'temurah_holiness_on_permanent_blemish': [('lands_no_exit_for_shearing',
                                                                                  None,
                                                                                  'Mishnah Temurah '
                                                                                  '2:3 — the '
                                                                                  'holiness lands '
                                                                                  'on a permanent '
                                                                                  'blemish; seat: '
                                                                                  'limb-sanctification '
                                                                                  'and individuals '
                                                                                  'only (LV27-04), '
                                                                                  'substitution '
                                                                                  'not transitive '
                                                                                  '(LV27-05), '
                                                                                  'disqualified '
                                                                                  'consecrated '
                                                                                  'beasts '
                                                                                  '(LV27-06), '
                                                                                  'unspecified to '
                                                                                  'upkeep '
                                                                                  '(LV27-09), '
                                                                                  'outwitting the '
                                                                                  'firstborn '
                                                                                  '(LV27-18), the '
                                                                                  "tithe's domain "
                                                                                  '(LV27-22)')],
                                       'temurah_inadvertent_as_deliberate': [('r_yosei_b_r_yehuda_yes',
                                                                              None,
                                                                              'Mishnah Temurah 2:3 '
                                                                              '— inadvertent as '
                                                                              'deliberate in '
                                                                              'substitution; seat: '
                                                                              'limb-sanctification '
                                                                              'and individuals '
                                                                              'only (LV27-04), '
                                                                              'substitution not '
                                                                              'transitive '
                                                                              '(LV27-05), '
                                                                              'disqualified '
                                                                              'consecrated beasts '
                                                                              '(LV27-06), '
                                                                              'unspecified to '
                                                                              'upkeep (LV27-09), '
                                                                              'outwitting the '
                                                                              'firstborn '
                                                                              '(LV27-18), the '
                                                                              "tithe's domain "
                                                                              '(LV27-22)')],
                                       'temurah_shelamim_offspring_class': [('as_shelamim_offered',
                                                                             'the Sages',
                                                                             'Mishnah Temurah 3:1 '
                                                                             "— a peace offering's "
                                                                             'offspring; seat: '
                                                                             'limb-sanctification '
                                                                             'and individuals only '
                                                                             '(LV27-04), '
                                                                             'substitution not '
                                                                             'transitive '
                                                                             '(LV27-05), '
                                                                             'disqualified '
                                                                             'consecrated beasts '
                                                                             '(LV27-06), '
                                                                             'unspecified to '
                                                                             'upkeep (LV27-09), '
                                                                             'outwitting the '
                                                                             'firstborn (LV27-18), '
                                                                             "the tithe's domain "
                                                                             '(LV27-22)'),
                                                                            ('r_eliezer_not_offered',
                                                                             'R. Eliezer',
                                                                             'Mishnah Temurah 3:1 '
                                                                             "— a peace offering's "
                                                                             'offspring; seat: '
                                                                             'limb-sanctification '
                                                                             'and individuals only '
                                                                             '(LV27-04), '
                                                                             'substitution not '
                                                                             'transitive '
                                                                             '(LV27-05), '
                                                                             'disqualified '
                                                                             'consecrated beasts '
                                                                             '(LV27-06), '
                                                                             'unspecified to '
                                                                             'upkeep (LV27-09), '
                                                                             'outwitting the '
                                                                             'firstborn (LV27-18), '
                                                                             "the tithe's domain "
                                                                             '(LV27-22)')],
                                       'temurah_female_for_olah_bore_male': [('graze_sell_bring_olah',
                                                                              'the first Tanna',
                                                                              'Mishnah Temurah 3:3 '
                                                                              '— one setting aside '
                                                                              'a female for an '
                                                                              'olah; seat: '
                                                                              'limb-sanctification '
                                                                              'and individuals '
                                                                              'only (LV27-04), '
                                                                              'substitution not '
                                                                              'transitive '
                                                                              '(LV27-05), '
                                                                              'disqualified '
                                                                              'consecrated beasts '
                                                                              '(LV27-06), '
                                                                              'unspecified to '
                                                                              'upkeep (LV27-09), '
                                                                              'outwitting the '
                                                                              'firstborn '
                                                                              '(LV27-18), the '
                                                                              "tithe's domain "
                                                                              '(LV27-22)'),
                                                                             ('r_eliezer_itself_offered',
                                                                              'R. Eliezer',
                                                                              'Mishnah Temurah 3:3 '
                                                                              '— one setting aside '
                                                                              'a female for an '
                                                                              'olah; seat: '
                                                                              'limb-sanctification '
                                                                              'and individuals '
                                                                              'only (LV27-04), '
                                                                              'substitution not '
                                                                              'transitive '
                                                                              '(LV27-05), '
                                                                              'disqualified '
                                                                              'consecrated beasts '
                                                                              '(LV27-06), '
                                                                              'unspecified to '
                                                                              'upkeep (LV27-09), '
                                                                              'outwitting the '
                                                                              'firstborn '
                                                                              '(LV27-18), the '
                                                                              "tithe's domain "
                                                                              '(LV27-22)')],
                                       'temurah_firstborn_tithe_substitute': [('as_source_eaten_blemished',
                                                                               None,
                                                                               'Mishnah Temurah '
                                                                               '3:5 — these are as '
                                                                               'firstborn and as '
                                                                               'tithe; seat: '
                                                                               'limb-sanctification '
                                                                               'and individuals '
                                                                               'only (LV27-04), '
                                                                               'substitution not '
                                                                               'transitive '
                                                                               '(LV27-05), '
                                                                               'disqualified '
                                                                               'consecrated beasts '
                                                                               '(LV27-06), '
                                                                               'unspecified to '
                                                                               'upkeep (LV27-09), '
                                                                               'outwitting the '
                                                                               'firstborn '
                                                                               '(LV27-18), the '
                                                                               "tithe's domain "
                                                                               '(LV27-22)')],
                                       'temurah_firstborn_tithe_redemption': [('none',
                                                                               None,
                                                                               'Mishnah Temurah '
                                                                               '3:5 — except the '
                                                                               'firstborn and the '
                                                                               'tithe; seat: '
                                                                               'limb-sanctification '
                                                                               'and individuals '
                                                                               'only (LV27-04), '
                                                                               'substitution not '
                                                                               'transitive '
                                                                               '(LV27-05), '
                                                                               'disqualified '
                                                                               'consecrated beasts '
                                                                               '(LV27-06), '
                                                                               'unspecified to '
                                                                               'upkeep (LV27-09), '
                                                                               'outwitting the '
                                                                               'firstborn '
                                                                               '(LV27-18), the '
                                                                               "tithe's domain "
                                                                               '(LV27-22)')],
                                       'temurah_outwitting_firstborn': [('sanctify_in_womb_by_sex',
                                                                         None,
                                                                         'Mishnah Temurah 5:1 — '
                                                                         'how does one outwit the '
                                                                         'firstborn; seat: '
                                                                         'limb-sanctification and '
                                                                         'individuals only '
                                                                         '(LV27-04), substitution '
                                                                         'not transitive '
                                                                         '(LV27-05), disqualified '
                                                                         'consecrated beasts '
                                                                         '(LV27-06), unspecified '
                                                                         'to upkeep (LV27-09), '
                                                                         'outwitting the firstborn '
                                                                         "(LV27-18), the tithe's "
                                                                         'domain (LV27-22)')],
                                       'temurah_two_males_born': [('one_olah_other_sold_profane',
                                                                   None,
                                                                   'Mishnah Temurah 5:2 — she bore '
                                                                   'two males; seat: '
                                                                   'limb-sanctification and '
                                                                   'individuals only (LV27-04), '
                                                                   'substitution not transitive '
                                                                   '(LV27-05), disqualified '
                                                                   'consecrated beasts (LV27-06), '
                                                                   'unspecified to upkeep '
                                                                   '(LV27-09), outwitting the '
                                                                   'firstborn (LV27-18), the '
                                                                   "tithe's domain (LV27-22)")],
                                       'temurah_utterance_order': [('r_meir_first_name_wins',
                                                                    'R. Meir',
                                                                    'Mishnah Temurah 5:3 — one '
                                                                    'saying: her offspring is an '
                                                                    'olah; seat: '
                                                                    'limb-sanctification and '
                                                                    'individuals only (LV27-04), '
                                                                    'substitution not transitive '
                                                                    '(LV27-05), disqualified '
                                                                    'consecrated beasts (LV27-06), '
                                                                    'unspecified to upkeep '
                                                                    '(LV27-09), outwitting the '
                                                                    'firstborn (LV27-18), the '
                                                                    "tithe's domain (LV27-22)"),
                                                                   ('r_yosei_intent_from_start',
                                                                    'R. Yosei',
                                                                    'Mishnah Temurah 5:3 — one '
                                                                    'saying: her offspring is an '
                                                                    'olah; seat: '
                                                                    'limb-sanctification and '
                                                                    'individuals only (LV27-04), '
                                                                    'substitution not transitive '
                                                                    '(LV27-05), disqualified '
                                                                    'consecrated beasts (LV27-06), '
                                                                    'unspecified to upkeep '
                                                                    '(LV27-09), outwitting the '
                                                                    'firstborn (LV27-18), the '
                                                                    "tithe's domain (LV27-22)")],
                                       'temurah_substitute_of_olah_and_shelamim': [('r_meir_olah',
                                                                                    'R. Meir',
                                                                                    'Mishnah '
                                                                                    'Temurah 5:4 — '
                                                                                    'the '
                                                                                    'substitute of '
                                                                                    'an olah and '
                                                                                    'of a peace '
                                                                                    'offering; '
                                                                                    'seat: '
                                                                                    'limb-sanctification '
                                                                                    'and '
                                                                                    'individuals '
                                                                                    'only '
                                                                                    '(LV27-04), '
                                                                                    'substitution '
                                                                                    'not '
                                                                                    'transitive '
                                                                                    '(LV27-05), '
                                                                                    'disqualified '
                                                                                    'consecrated '
                                                                                    'beasts '
                                                                                    '(LV27-06), '
                                                                                    'unspecified '
                                                                                    'to upkeep '
                                                                                    '(LV27-09), '
                                                                                    'outwitting '
                                                                                    'the firstborn '
                                                                                    '(LV27-18), '
                                                                                    "the tithe's "
                                                                                    'domain '
                                                                                    '(LV27-22)'),
                                                                                   ('r_yosei_intent_both',
                                                                                    'R. Yosei',
                                                                                    'Mishnah '
                                                                                    'Temurah 5:4 — '
                                                                                    'the '
                                                                                    'substitute of '
                                                                                    'an olah and '
                                                                                    'of a peace '
                                                                                    'offering; '
                                                                                    'seat: '
                                                                                    'limb-sanctification '
                                                                                    'and '
                                                                                    'individuals '
                                                                                    'only '
                                                                                    '(LV27-04), '
                                                                                    'substitution '
                                                                                    'not '
                                                                                    'transitive '
                                                                                    '(LV27-05), '
                                                                                    'disqualified '
                                                                                    'consecrated '
                                                                                    'beasts '
                                                                                    '(LV27-06), '
                                                                                    'unspecified '
                                                                                    'to upkeep '
                                                                                    '(LV27-09), '
                                                                                    'outwitting '
                                                                                    'the firstborn '
                                                                                    '(LV27-18), '
                                                                                    "the tithe's "
                                                                                    'domain '
                                                                                    '(LV27-22)')],
                                       'temurah_formulas': [('instead_substitute_exchange_yes_desanctified_no',
                                                             None,
                                                             'Mishnah Temurah 5:5 — this instead '
                                                             'of that; seat: limb-sanctification '
                                                             'and individuals only (LV27-04), '
                                                             'substitution not transitive '
                                                             '(LV27-05), disqualified consecrated '
                                                             'beasts (LV27-06), unspecified to '
                                                             'upkeep (LV27-09), outwitting the '
                                                             "firstborn (LV27-18), the tithe's "
                                                             'domain (LV27-22)')],
                                       'temurah_unnamed_object': [('said_nothing',
                                                                   None,
                                                                   'Mishnah Temurah 5:6 — instead '
                                                                   'of a sin offering — he said '
                                                                   'nothing; seat: '
                                                                   'limb-sanctification and '
                                                                   'individuals only (LV27-04), '
                                                                   'substitution not transitive '
                                                                   '(LV27-05), disqualified '
                                                                   'consecrated beasts (LV27-06), '
                                                                   'unspecified to upkeep '
                                                                   '(LV27-09), outwitting the '
                                                                   'firstborn (LV27-18), the '
                                                                   "tithe's domain (LV27-22)")],
                                       'temurah_altar_holy_vs_upkeep': [('altar_substitutes_upkeep_not',
                                                                         None,
                                                                         'Mishnah Temurah 7:1 — '
                                                                         "the altar's "
                                                                         'consecrations make '
                                                                         'substitutes; seat: '
                                                                         'limb-sanctification and '
                                                                         'individuals only '
                                                                         '(LV27-04), substitution '
                                                                         'not transitive '
                                                                         '(LV27-05), disqualified '
                                                                         'consecrated beasts '
                                                                         '(LV27-06), unspecified '
                                                                         'to upkeep (LV27-09), '
                                                                         'outwitting the firstborn '
                                                                         "(LV27-18), the tithe's "
                                                                         'domain (LV27-22)')],
                                       'temurah_unspecified_consecration': [('to_upkeep',
                                                                             None,
                                                                             'Mishnah Temurah 7:2 '
                                                                             '— unspecified '
                                                                             'consecrations to the '
                                                                             'upkeep; seat: '
                                                                             'limb-sanctification '
                                                                             'and individuals only '
                                                                             '(LV27-04), '
                                                                             'substitution not '
                                                                             'transitive '
                                                                             '(LV27-05), '
                                                                             'disqualified '
                                                                             'consecrated beasts '
                                                                             '(LV27-06), '
                                                                             'unspecified to '
                                                                             'upkeep (LV27-09), '
                                                                             'outwitting the '
                                                                             'firstborn (LV27-18), '
                                                                             "the tithe's domain "
                                                                             '(LV27-22)')],
                                       'temurah_consecrated_died': [('buried',
                                                                     'the first Tanna',
                                                                     'Mishnah Temurah 7:3 — and if '
                                                                     'they died they are buried; '
                                                                     'seat: limb-sanctification '
                                                                     'and individuals only '
                                                                     '(LV27-04), substitution not '
                                                                     'transitive (LV27-05), '
                                                                     'disqualified consecrated '
                                                                     'beasts (LV27-06), '
                                                                     'unspecified to upkeep '
                                                                     '(LV27-09), outwitting the '
                                                                     'firstborn (LV27-18), the '
                                                                     "tithe's domain (LV27-22)"),
                                                                    ('r_shimon_upkeep_redeemed',
                                                                     'R. Shimon',
                                                                     'Mishnah Temurah 7:3 — and if '
                                                                     'they died they are buried; '
                                                                     'seat: limb-sanctification '
                                                                     'and individuals only '
                                                                     '(LV27-04), substitution not '
                                                                     'transitive (LV27-05), '
                                                                     'disqualified consecrated '
                                                                     'beasts (LV27-06), '
                                                                     'unspecified to upkeep '
                                                                     '(LV27-09), outwitting the '
                                                                     'firstborn (LV27-18), the '
                                                                     "tithe's domain (LV27-22)")]}},
 'bekhorot_tithe_file': {'tractate': 'Bekhorot',
                         'oracle': 'Mishnah Bekhorot 9:2; 9:3; 9:4; 9:5; 9:6; 9:8',
                         'claim': 'LV27-23',
                         'anchor': 'Lev.27.32-33 (lev_27_vows_valuations, LV27-03, LV27-06, '
                                   'LV27-22, LV27-23)',
                         'cells': {'maaser_behemah_joining_distance': [('sixteen_mil',
                                                                        None,
                                                                        'Mishnah Bekhorot 9:2 — '
                                                                        'sixteen mil; seat: the '
                                                                        'four clocks (LV27-03), '
                                                                        'disqualified beasts '
                                                                        "(LV27-06), the tithe's "
                                                                        'domain (LV27-22), the '
                                                                        'passing predicate and the '
                                                                        'error rule (LV27-23) — '
                                                                        'the naming machine '
                                                                        'compiled this sitting in '
                                                                        'cold_run_yovel.py')],
                                   'maaser_behemah_jordan_divides': [('r_meir_yes',
                                                                      None,
                                                                      'Mishnah Bekhorot 9:2 — the '
                                                                      'Jordan divides; seat: the '
                                                                      'four clocks (LV27-03), '
                                                                      'disqualified beasts '
                                                                      "(LV27-06), the tithe's "
                                                                      'domain (LV27-22), the '
                                                                      'passing predicate and the '
                                                                      'error rule (LV27-23) — the '
                                                                      'naming machine compiled '
                                                                      'this sitting in '
                                                                      'cold_run_yovel.py')],
                                   'maaser_behemah_bought_or_gifted': [('exempt',
                                                                        None,
                                                                        'Mishnah Bekhorot 9:3 — '
                                                                        'the bought or the gifted '
                                                                        'is exempt; seat: the four '
                                                                        'clocks (LV27-03), '
                                                                        'disqualified beasts '
                                                                        "(LV27-06), the tithe's "
                                                                        'domain (LV27-22), the '
                                                                        'passing predicate and the '
                                                                        'error rule (LV27-23) — '
                                                                        'the naming machine '
                                                                        'compiled this sitting in '
                                                                        'cold_run_yovel.py')],
                                   'maaser_behemah_partners_surcharge': [('inverse_of_surcharge',
                                                                          None,
                                                                          'Mishnah Bekhorot 9:3 — '
                                                                          'liable to the '
                                                                          'surcharge, exempt from '
                                                                          'the tithe; seat: the '
                                                                          'four clocks (LV27-03), '
                                                                          'disqualified beasts '
                                                                          "(LV27-06), the tithe's "
                                                                          'domain (LV27-22), the '
                                                                          'passing predicate and '
                                                                          'the error rule '
                                                                          '(LV27-23) — the naming '
                                                                          'machine compiled this '
                                                                          'sitting in '
                                                                          'cold_run_yovel.py')],
                                   'maaser_behemah_excluded_kinds': [('kilayim_terefah_caesarean_underage_orphan',
                                                                      None,
                                                                      'Mishnah Bekhorot 9:4 — '
                                                                      'except the mixed kinds and '
                                                                      'the torn; seat: the four '
                                                                      'clocks (LV27-03), '
                                                                      'disqualified beasts '
                                                                      "(LV27-06), the tithe's "
                                                                      'domain (LV27-22), the '
                                                                      'passing predicate and the '
                                                                      'error rule (LV27-23) — the '
                                                                      'naming machine compiled '
                                                                      'this sitting in '
                                                                      'cold_run_yovel.py')],
                                   'maaser_behemah_orphan_definition': [('mother_died_or_slaughtered',
                                                                         'the first Tanna',
                                                                         'Mishnah Bekhorot 9:4 — '
                                                                         'what is an orphan; seat: '
                                                                         'the four clocks '
                                                                         '(LV27-03), disqualified '
                                                                         'beasts (LV27-06), the '
                                                                         "tithe's domain "
                                                                         '(LV27-22), the passing '
                                                                         'predicate and the error '
                                                                         'rule (LV27-23) — the '
                                                                         'naming machine compiled '
                                                                         'this sitting in '
                                                                         'cold_run_yovel.py'),
                                                                        ('r_yehoshua_hide_intact_not_orphan',
                                                                         'R. Yehoshua',
                                                                         'Mishnah Bekhorot 9:4 — '
                                                                         'what is an orphan; seat: '
                                                                         'the four clocks '
                                                                         '(LV27-03), disqualified '
                                                                         'beasts (LV27-06), the '
                                                                         "tithe's domain "
                                                                         '(LV27-22), the passing '
                                                                         'predicate and the error '
                                                                         'rule (LV27-23) — the '
                                                                         'naming machine compiled '
                                                                         'this sitting in '
                                                                         'cold_run_yovel.py')],
                                   'maaser_behemah_threshing_seasons': [('r_akiva_festival_eves',
                                                                         'R. Akiva',
                                                                         'Mishnah Bekhorot 9:5 — '
                                                                         'three threshing seasons '
                                                                         'for the animal tithe; '
                                                                         'seat: the four clocks '
                                                                         '(LV27-03), disqualified '
                                                                         'beasts (LV27-06), the '
                                                                         "tithe's domain "
                                                                         '(LV27-22), the passing '
                                                                         'predicate and the error '
                                                                         'rule (LV27-23) — the '
                                                                         'naming machine compiled '
                                                                         'this sitting in '
                                                                         'cold_run_yovel.py'),
                                                                        ('ben_azzai_dates',
                                                                         'ben Azzai',
                                                                         'Mishnah Bekhorot 9:5 — '
                                                                         'three threshing seasons '
                                                                         'for the animal tithe; '
                                                                         'seat: the four clocks '
                                                                         '(LV27-03), disqualified '
                                                                         'beasts (LV27-06), the '
                                                                         "tithe's domain "
                                                                         '(LV27-22), the passing '
                                                                         'predicate and the error '
                                                                         'rule (LV27-23) — the '
                                                                         'naming machine compiled '
                                                                         'this sitting in '
                                                                         'cold_run_yovel.py'),
                                                                        ('r_eliezer_r_shimon_dates',
                                                                         'R. Eliezer and R. Shimon',
                                                                         'Mishnah Bekhorot 9:5 — '
                                                                         'three threshing seasons '
                                                                         'for the animal tithe; '
                                                                         'seat: the four clocks '
                                                                         '(LV27-03), disqualified '
                                                                         'beasts (LV27-06), the '
                                                                         "tithe's domain "
                                                                         '(LV27-22), the passing '
                                                                         'predicate and the error '
                                                                         'rule (LV27-23) — the '
                                                                         'naming machine compiled '
                                                                         'this sitting in '
                                                                         'cold_run_yovel.py')],
                                   'maaser_behemah_new_year': [('r_meir_first_of_elul',
                                                                'R. Meir',
                                                                'Mishnah Bekhorot 9:5 — the first '
                                                                'of Elul is the new year for the '
                                                                'animal tithe; seat: the four '
                                                                'clocks (LV27-03), disqualified '
                                                                "beasts (LV27-06), the tithe's "
                                                                'domain (LV27-22), the passing '
                                                                'predicate and the error rule '
                                                                '(LV27-23) — the naming machine '
                                                                'compiled this sitting in '
                                                                'cold_run_yovel.py'),
                                                               ('first_of_tishrei',
                                                                'R. Eliezer and R. Shimon',
                                                                'Mishnah Bekhorot 9:5 — the first '
                                                                'of Elul is the new year for the '
                                                                'animal tithe; seat: the four '
                                                                'clocks (LV27-03), disqualified '
                                                                "beasts (LV27-06), the tithe's "
                                                                'domain (LV27-22), the passing '
                                                                'predicate and the error rule '
                                                                '(LV27-23) — the naming machine '
                                                                'compiled this sitting in '
                                                                'cold_run_yovel.py')],
                                   'maaser_behemah_year_boundary': [('same_year_combines',
                                                                     None,
                                                                     'Mishnah Bekhorot 9:6 — all '
                                                                     'born from the first of '
                                                                     'Tishrei; seat: the four '
                                                                     'clocks (LV27-03), '
                                                                     'disqualified beasts '
                                                                     "(LV27-06), the tithe's "
                                                                     'domain (LV27-22), the '
                                                                     'passing predicate and the '
                                                                     'error rule (LV27-23) — the '
                                                                     'naming machine compiled this '
                                                                     'sitting in '
                                                                     'cold_run_yovel.py')],
                                   'maaser_behemah_season_office': [('before_free_after_no_slaughter',
                                                                     None,
                                                                     'Mishnah Bekhorot 9:6 — the '
                                                                     'season arrived — he may not '
                                                                     'slaughter; seat: the four '
                                                                     'clocks (LV27-03), '
                                                                     'disqualified beasts '
                                                                     "(LV27-06), the tithe's "
                                                                     'domain (LV27-22), the '
                                                                     'passing predicate and the '
                                                                     'error rule (LV27-23) — the '
                                                                     'naming machine compiled this '
                                                                     'sitting in '
                                                                     'cold_run_yovel.py')],
                                   'maaser_behemah_two_out_as_one': [('count_two_by_two',
                                                                      None,
                                                                      'Mishnah Bekhorot 9:8 — two '
                                                                      'came out as one; seat: the '
                                                                      'four clocks (LV27-03), '
                                                                      'disqualified beasts '
                                                                      "(LV27-06), the tithe's "
                                                                      'domain (LV27-22), the '
                                                                      'passing predicate and the '
                                                                      'error rule (LV27-23) — the '
                                                                      'naming machine compiled '
                                                                      'this sitting in '
                                                                      'cold_run_yovel.py')],
                                   'maaser_behemah_error_ninth_tenth_eleventh': [('all_three_sanctified',
                                                                                  None,
                                                                                  'Mishnah '
                                                                                  'Bekhorot 9:8 — '
                                                                                  'all three are '
                                                                                  'sanctified; '
                                                                                  'seat: the four '
                                                                                  'clocks '
                                                                                  '(LV27-03), '
                                                                                  'disqualified '
                                                                                  'beasts '
                                                                                  '(LV27-06), the '
                                                                                  "tithe's domain "
                                                                                  '(LV27-22), the '
                                                                                  'passing '
                                                                                  'predicate and '
                                                                                  'the error rule '
                                                                                  '(LV27-23) — the '
                                                                                  'naming machine '
                                                                                  'compiled this '
                                                                                  'sitting in '
                                                                                  'cold_run_yovel.py')],
                                   'maaser_behemah_eleventh_status': [('r_meir_shelamim_makes_substitute',
                                                                       'R. Meir',
                                                                       'Mishnah Bekhorot 9:8 — and '
                                                                       'the eleventh is offered a '
                                                                       'peace offering; seat: the '
                                                                       'four clocks (LV27-03), '
                                                                       'disqualified beasts '
                                                                       "(LV27-06), the tithe's "
                                                                       'domain (LV27-22), the '
                                                                       'passing predicate and the '
                                                                       'error rule (LV27-23) — the '
                                                                       'naming machine compiled '
                                                                       'this sitting in '
                                                                       'cold_run_yovel.py'),
                                                                      ('r_yehuda_questions_substitute',
                                                                       'R. Yehuda',
                                                                       'Mishnah Bekhorot 9:8 — and '
                                                                       'the eleventh is offered a '
                                                                       'peace offering; seat: the '
                                                                       'four clocks (LV27-03), '
                                                                       'disqualified beasts '
                                                                       "(LV27-06), the tithe's "
                                                                       'domain (LV27-22), the '
                                                                       'passing predicate and the '
                                                                       'error rule (LV27-23) — the '
                                                                       'naming machine compiled '
                                                                       'this sitting in '
                                                                       'cold_run_yovel.py')],
                                   'maaser_behemah_eleventh_rule': [('only_if_tenth_name_uprooted',
                                                                     None,
                                                                     'Mishnah Bekhorot 9:8 — '
                                                                     'wherever the name tenth was '
                                                                     'not uprooted from it; seat: '
                                                                     'the four clocks (LV27-03), '
                                                                     'disqualified beasts '
                                                                     "(LV27-06), the tithe's "
                                                                     'domain (LV27-22), the '
                                                                     'passing predicate and the '
                                                                     'error rule (LV27-23) — the '
                                                                     'naming machine compiled this '
                                                                     'sitting in '
                                                                     'cold_run_yovel.py')]}},
 'ribbit_file': {'tractate': 'Bava Metzia',
                 'oracle': 'Mishnah Bava Metzia 5:2; 5:3; 5:4; 5:5; 5:6; 5:7; 5:8; 5:9; 5:10',
                 'claim': 'LV25B-14',
                 'anchor': 'Lev.25.35-38 (lev_25_redeem_poor, LV25B-14)',
                 'cells': {'ribbit_lender_dwells_free': [('forbidden_interest',
                                                          None,
                                                          'Mishnah Bava Metzia 5:2 — he may not '
                                                          'dwell in his courtyard free; seat: the '
                                                          'interest definitions and the one flask '
                                                          "(LV25B-14); the foreigner's scope an "
                                                          'import edge from Deuteronomy 23:21')],
                           'ribbit_increase_on_rent_vs_sale': [('rent_permitted_sale_forbidden',
                                                                None,
                                                                'Mishnah Bava Metzia 5:2 — '
                                                                'increase on rent, no increase on '
                                                                'sale; seat: the interest '
                                                                'definitions and the one flask '
                                                                "(LV25B-14); the foreigner's scope "
                                                                'an import edge from Deuteronomy '
                                                                '23:21')],
                           'ribbit_field_forfeit_after_three_years': [('permitted_boethus',
                                                                       None,
                                                                       'Mishnah Bava Metzia 5:3 — '
                                                                       'and so Boethus b. Zonin '
                                                                       'did; seat: the interest '
                                                                       'definitions and the one '
                                                                       'flask (LV25B-14); the '
                                                                       "foreigner's scope an "
                                                                       'import edge from '
                                                                       'Deuteronomy 23:21')],
                           'ribbit_shopkeeper_half_profit': [('forbidden_unless_laborers_wage',
                                                              None,
                                                              'Mishnah Bava Metzia 5:4 — no '
                                                              'shopkeeper set for half the profit; '
                                                              'seat: the interest definitions and '
                                                              'the one flask (LV25B-14); the '
                                                              "foreigner's scope an import edge "
                                                              'from Deuteronomy 23:21')],
                           'ribbit_calves_at_half': [('accepted_raised_to_a_third',
                                                      None,
                                                      'Mishnah Bava Metzia 5:4 — raised until they '
                                                      'reach a third; seat: the interest '
                                                      'definitions and the one flask (LV25B-14); '
                                                      "the foreigner's scope an import edge from "
                                                      'Deuteronomy 23:21')],
                           'ribbit_appraise_working_animal': [('permitted_at_half',
                                                               None,
                                                               'Mishnah Bava Metzia 5:5 — they '
                                                               'appraise a cow and a donkey; seat: '
                                                               'the interest definitions and the '
                                                               'one flask (LV25B-14); the '
                                                               "foreigner's scope an import edge "
                                                               'from Deuteronomy 23:21')],
                           'ribbit_iron_sheep': [('israelite_forbidden_gentile_permitted',
                                                  None,
                                                  'Mishnah Bava Metzia 5:6 — iron sheep not '
                                                  'accepted from an Israelite; seat: the interest '
                                                  'definitions and the one flask (LV25B-14); the '
                                                  "foreigner's scope an import edge from "
                                                  'Deuteronomy 23:21')],
                           'ribbit_lending_gentiles_money': [('with_gentiles_knowledge',
                                                              None,
                                                              'Mishnah Bava Metzia 5:6 — with the '
                                                              "gentile's knowledge; seat: the "
                                                              'interest definitions and the one '
                                                              "flask (LV25B-14); the foreigner's "
                                                              'scope an import edge from '
                                                              'Deuteronomy 23:21')],
                           'ribbit_forward_price': [('not_before_market_rate',
                                                     None,
                                                     'Mishnah Bava Metzia 5:7 — no price is fixed '
                                                     'on produce until the rate is out; seat: the '
                                                     'interest definitions and the one flask '
                                                     "(LV25B-14); the foreigner's scope an import "
                                                     'edge from Deuteronomy 23:21')],
                           'ribbit_first_to_reapers': [('may_fix_on_stack',
                                                        None,
                                                        'Mishnah Bava Metzia 5:7 — he fixes with '
                                                        'him on the stack; seat: the interest '
                                                        'definitions and the one flask (LV25B-14); '
                                                        "the foreigner's scope an import edge from "
                                                        'Deuteronomy 23:21')],
                           'ribbit_wheat_for_wheat_sharecroppers': [('seed_yes_food_no',
                                                                     None,
                                                                     'Mishnah Bava Metzia 5:8 — '
                                                                     'wheat for wheat for seed; '
                                                                     'seat: the interest '
                                                                     'definitions and the one '
                                                                     'flask (LV25B-14); the '
                                                                     "foreigner's scope an import "
                                                                     'edge from Deuteronomy '
                                                                     '23:21')],
                           'ribbit_lend_kor_until_threshing': [('forbidden_until_son_comes_permitted',
                                                                'the first Tanna',
                                                                'Mishnah Bava Metzia 5:9 — lend me '
                                                                'a kor of wheat; seat: the '
                                                                'interest definitions and the one '
                                                                "flask (LV25B-14); the foreigner's "
                                                                'scope an import edge from '
                                                                'Deuteronomy 23:21'),
                                                               ('hillel_forbids',
                                                                'Hillel',
                                                                'Mishnah Bava Metzia 5:9 — lend me '
                                                                'a kor of wheat; seat: the '
                                                                'interest definitions and the one '
                                                                "flask (LV25B-14); the foreigner's "
                                                                'scope an import edge from '
                                                                'Deuteronomy 23:21')],
                           'ribbit_labor_exchange': [('same_labor_same_season_only',
                                                      None,
                                                      'Mishnah Bava Metzia 5:10 — weed with me and '
                                                      'I will weed with you; seat: the interest '
                                                      'definitions and the one flask (LV25B-14); '
                                                      "the foreigner's scope an import edge from "
                                                      'Deuteronomy 23:21')],
                           'ribbit_advance_and_after': [('rabban_gamliel_both_named',
                                                         None,
                                                         'Mishnah Bava Metzia 5:10 — there is '
                                                         'advance interest and there is '
                                                         'after-interest; seat: the interest '
                                                         'definitions and the one flask '
                                                         "(LV25B-14); the foreigner's scope an "
                                                         'import edge from Deuteronomy 23:21')],
                           'ribbit_of_words': [('r_shimon_named',
                                                None,
                                                'Mishnah Bava Metzia 5:10 — there is interest of '
                                                'words; seat: the interest definitions and the one '
                                                "flask (LV25B-14); the foreigner's scope an import "
                                                'edge from Deuteronomy 23:21')]}}}


def build(V):
    rules = {}
    for mod, spec in TABLE.items():
        prov = dict(talmud_source=spec["oracle"], exodus_anchor=spec["anchor"])

        def make(spec=spec, prov=prov):
            def fn(case):
                arms = spec["cells"].get(case.get("query"))
                if not arms:
                    return None
                return [V(v, b, authority=a, machine_claim=spec["claim"], **prov)
                        for v, a, b in arms]
            return fn
        rules[mod] = {"fn": make(), "tractate": spec["tractate"]}
    return rules

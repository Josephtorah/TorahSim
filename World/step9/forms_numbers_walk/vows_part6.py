

# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows).
# =====================================================================
CASES = [
    # F1 — the man
    ('Num 30:2 / Sifrei 153:2; Bava Batra 120b:1 — the frame: Moses\' voice, for all generations', lambda: the_man({'ask': 'frame'}, DATA), 'a law relayed in Moses\' voice — this is the thing which the LORD commanded, for all generations'),
    ('Num 30:2 / Sifrei 153:2; Nedarim 77b:8-78a:1 — two offices, two verbs', lambda: the_man({'ask': 'this_is_the_thing'}, DATA), 'two offices, two verbs — the husband annuls, the sage dissolves; the words crossed say nothing'),
    ('Num 30:2 / Sifrei 153:1; Nedarim 78b:3 — the heads of the tribes', lambda: the_man({'ask': 'heads_of_the_tribes'}, DATA), 'the sage\'s release — one expert or three laymen: the shelf\'s office on the freed phrase'),
    ('Mishnah Chagigah 1:8; Chagigah 10a:13 — the release flies in the air; Shmuel\'s ground', lambda: the_man({'ask': 'sage_release_flies'}, DATA), 'flies in the air — the one unrefuted ground the chapter\'s own clause 30:3'),
    ('Nedarim 77b:2-3 — the sage standing, alone, at night', lambda: the_man({'ask': 'sage_release_form'}, DATA), 'no session, no court — standing, alone, at night; the regret arm recorded'),
    ('Nedarim 65a:1-4 — in the presence of the one vowed against', lambda: the_man({'ask': 'sage_release_presence'}, DATA), 'dissolved in the presence of the one vowed against'),
    ('Nedarim 90a:3, 90b:4 — only a vow in effect', lambda: the_man({'ask': 'sage_release_timing'}, DATA), 'only a vow in effect is dissolved'),
    ('Mishnah Nedarim 9:1-10 — the openings', lambda: the_man({'ask': 'openings'}, DATA), 'an opening on "had I known" — the answer sheet\'s method, never the ink\'s'),
    ('Mishnah Nedarim 9:10; Nedarim 65a:6 — the mistaken vow', lambda: the_man({'ask': 'mistaken_vow'}, DATA), 'a mistaken vow — no vow'),
    ('Mishnah Niddah 5:6 — a girl of ten', lambda: the_man({'ask': 'age', 'age': 10, 'sex': 'girl'}, DATA), 'a minor — no vow, no consecration (even saying "we know")'),
    ('Mishnah Niddah 5:6 — a girl of eleven and a day who knows', lambda: the_man({'ask': 'age', 'age': 11, 'sex': 'girl', 'knows_to_whom': True}, DATA), 'the examined year — bound if she knows in Whose name'),
    ('Mishnah Niddah 5:6 — a boy of twelve and a day who does not know', lambda: the_man({'ask': 'age', 'age': 12, 'sex': 'boy', 'knows_to_whom': False}, DATA), 'the examined year — she does not know in Whose name: no vow'),
    ('Mishnah Niddah 5:6; Niddah 46a:2 — a boy of thirteen and a day (NS by CALL)', lambda: the_man({'ask': 'age', 'age': 13, 'sex': 'boy'}, DATA), 'of age — the vow stands without examination'),
    ('Nedarim 13b:4; Shevuot 25a:11-12 — the two stringencies', lambda: the_man({'ask': 'vow_vs_oath'}, DATA), 'the vow binds the OBJECT (even a mitzva\'s), the oath binds the PERSON (even to nothing tangible)'),
    ('Nedarim 14a:5 — leaning on a vowed thing', lambda: the_man({'ask': 'vow_support', 'base': 'vowed'}, DATA), 'leans on a vowed thing — bound'),
    ('Mishnah Nedarim 2:1; Nedarim 13a:2 — leaning on carrion', lambda: the_man({'ask': 'vow_support', 'base': 'torah_forbidden'}, DATA), 'leans on a Torah-forbidden thing — no vow'),
    ('Mishnah Nedarim 1:2 — the substitutes', lambda: the_man({'ask': 'substitutes'}, DATA), 'the substitutes bind — the nations\' words or the Sages\' devised ones'),
    ('Mishnah Nedarim 1:3; Nedarim 11b:6 — not non-sacred', lambda: the_man({'ask': 'not_non_sacred'}, DATA), 'the negation of the common binds — "not non-sacred" is an offering'),
    ('Mishnah Nedarim 1:4; Nedarim 13b:5 — the vow on a limb', lambda: the_man({'ask': 'on_a_limb'}, DATA), 'a vow on the limb binds; on the act it would not'),
    ('Sifrei 153:4; Shevuot 27a:1-5; Nedarim 16b:3 — bind the permitted', lambda: the_man({'ask': 'bind_the_permitted'}, DATA), 'no oath to permit the forbidden — the oath void'),
    ('Num 30:3 / Sifrei 153:4; Nedarim 81b:5, 15a:8 — he shall not profane his word', lambda: the_man({'ask': 'not_profane'}, DATA), 'the vower bound to his word; the sage not for himself; the custom a quasi-vow'),
    ('Sifrei 153:4; Nedarim 3a:7; the musafim runner by CALL — the two transgressions', lambda: the_man({'ask': 'two_transgressions'}, DATA), 'profane and delay — two transgressions; the delay counted in festivals by call'),
    ('Rosh Hashanah 4a:13-4b:2, 6a:14, 6a:16 — the delay\'s clocks', lambda: the_man({'ask': 'delay_clocks'}, DATA), 'two dues — the positive at the first festival, the prohibition at the third; charity now'),
    ('Rosh Hashanah 5b:5, 6a:3 — the sin in you', lambda: the_man({'ask': 'sin_in_you'}, DATA), 'the delay\'s sin on the vower alone — the offering and the wife unmoved'),
    ('Rosh Hashanah 6a:12 — the vow and the gift', lambda: the_man({'ask': 'vow_vs_gift'}, DATA), 'the vow\'s debit persists past its object; the gift\'s dies with it'),
    ('Shevuot 26b:9, 26b:15-16; Sifrei 153:4 — the lips or the heart', lambda: the_man({'ask': 'lips_or_heart'}, DATA), 'the lips required — the heart\'s vow the Sifrei\'s arm, recorded'),
    ('Nedarim 77b:4, 10a:9 — the vower a sinner', lambda: the_man({'ask': 'vower_a_sinner'}, DATA), 'the vower called a sinner — the vow\'s standing on the shelf'),
    ('Nazir 61a:8 — on his soul: the slave', lambda: the_man({'ask': 'on_his_soul'}, DATA), 'the slave\'s soul not his — no vow'),
    ('Shevuot 22a:9, 22a:2 — the konam\'s measure', lambda: the_man({'ask': 'konam_measure'}, DATA), 'any amount — the vow forbids the object, not the act'),
    ('Nedarim 3b:4 — the intimations', lambda: the_man({'ask': 'intimations'}, DATA), 'the partial formula binds — two sources for one rule'),
    ('Num 30:3 / Rosh Hashanah 6a:5 — all that proceeds out of his mouth', lambda: the_man({'ask': 'all_that_proceeds'}, DATA), 'the vow\'s fulfilment — a positive duty, a prohibition, and the court\'s compulsion on one clause'),
    # F2 — the daughter
    ('Num 30:4 / Sifrei 153:4 — a minor', lambda: the_daughter({'ask': 'in_her_youth', 'stage': 'minor'}, DATA), 'a minor — no vow'),
    ('Num 30:4 / Sifrei 153:4 — in her youth', lambda: the_daughter({'ask': 'in_her_youth', 'stage': 'youth'}, DATA), 'in her youth — under her father'),
    ('Mishnah Nedarim 10:2, 11:10 — the mature daughter', lambda: the_daughter({'ask': 'in_her_youth', 'stage': 'mature'}, DATA), 'mature — her vow stands, no annuller'),
    ('Sifrei 153:4; Nedarim 70a-70b — the father\'s domain', lambda: the_daughter({'ask': 'fathers_domain'}, DATA), 'the father\'s domain — the betrothal\'s widow in, the marriage\'s out'),
    ('Sifrei 153:5; Nedarim 72b:10 — the hearing by report', lambda: the_daughter({'ask': 'hearing_by_report'}, DATA), 'told by others — the hearing day opens'),
    ('Sifrei 153:5; Nedarim 73a:4 — the deaf', lambda: the_daughter({'ask': 'the_deaf'}, DATA), 'the deaf hear nothing — no hearing day, no annulment'),
    ('Sifrei 153:5; Mishnah Nedarim 11:5; Nedarim 86b:5 — intending her', lambda: the_daughter({'ask': 'intends_her'}, DATA), 'the annulment void — the intended vow only; he annuls again'),
    ('Sifrei 153:5; Nedarim 79a:1 — confirmed for one hour', lambda: the_daughter({'ask': 'confirmed_for_one_hour'}, DATA), 'confirmed once, never annulled'),
    ('Num 30:9 / Sifrei 153:6, 153:9 — restraint is annulment', lambda: the_daughter({'ask': 'restraint_is_annulment'}, DATA), 'restraint = annulment — the word defined by its pair'),
    ('Sifrei 153:6 — the father\'s hearing day by the likening', lambda: the_daughter({'ask': 'fathers_hearing_day'}, DATA), 'the father\'s day by the footer\'s likening'),
    ('Sifrei 153:6; Kiddushin 81b:5; Nazir 23a:3; Nedarim 83a:1 — the forgiveness', lambda: the_daughter({'ask': 'forgiveness'}, DATA), 'annulled unknown to her — forgiven for the intent, no lashes'),
    ('Sifrei 153:6; Bava Metzia 96a:20; Nedarim 72b:8-9 — the caretaker and the messenger', lambda: the_daughter({'ask': 'caretaker'}, DATA), 'the act his own — the messenger a recorded dispute'),
    ('Nedarim 72b:3-73a:1 — annulment without hearing (unresolved)', lambda: the_daughter({'ask': 'annulment_without_hearing'}, DATA), 'unresolved on the shelf — the hearing the machine\'s trigger'),
    ('Sifrei 155:1 — the father\'s scope; I reasoned and reversed', lambda: the_daughter({'ask': 'fathers_scope'}, DATA), 'the father as the husband by the likening — the reversed induction named'),
    ('Ketubot 46b:6, 47a:6; Kiddushin 3b:7 — the father\'s rights from the footer', lambda: the_daughter({'ask': 'fathers_rights'}, DATA), 'the footer\'s clause carried to her gains — labeled'),
    ('Nedarim 79a:1; 77b:7 — the annulment in the heart', lambda: the_daughter({'ask': 'heart_annuls'}, DATA), 'the annulment an act — the heart\'s arm recorded'),
    # F3 — the betrothed
    ('Mishnah Nedarim 10:1; Nedarim 67a:5, 68a:1 — both together', lambda: the_betrothed({'ask': 'joint_authority', 'by': ['father', 'husband']}, DATA), 'annulled — both together'),
    ('Mishnah Nedarim 10:1 — the father alone', lambda: the_betrothed({'ask': 'joint_authority', 'by': ['father']}, DATA), 'not annulled — one alone'),
    ('Num 30:7 / Nedarim 67b:2, 70a:8, 70b:1 — be, she shall be', lambda: the_betrothed({'ask': 'be_she_shall_be'}, DATA), 'the doubled verb read as law — betrothal, and the second betrothal after the first\'s death'),
    ('Mishnah Nedarim 10:2; Nedarim 70a:7 — the father dies', lambda: the_betrothed({'ask': 'fathers_death'}, DATA), 'the father dead — the betrothed alone annuls nothing; the vow stands'),
    ('Mishnah Nedarim 10:2; Nedarim 68a:5 — the betrothed dies unheard', lambda: the_betrothed({'ask': 'betrotheds_death', 'husband': 'unheard'}, DATA), 'reverted to the father — he annuls alone'),
    ('Nedarim 68b:1 — the betrothed died silent the next day', lambda: the_betrothed({'ask': 'betrotheds_death', 'husband': 'silent_next_day'}, DATA), 'confirmed before his death — the father cannot'),
    ('Num 30:7 / Nedarim 71a:2-3; Mishnah Nedarim 10:3 — the vows carried', lambda: the_betrothed({'ask': 'vows_carried'}, DATA), 'the vows carried to the last betrothed — annulled with the father'),
    ('Nedarim 69a:2, 71b:1 — Beit Hillel: the annulment weakens', lambda: the_betrothed({'ask': 'share_or_weaken'}, DATA), 'the joint annulment weakens, never severs'),
    ('Nedarim 67b:4 — the father\'s confirmation blocks', lambda: the_betrothed({'ask': 'fathers_confirmation'}, DATA), 'one confirming — confirmed'),
    ('Nedarim 67a:4 — the dissolved confirmation', lambda: the_betrothed({'ask': 'dissolved_confirmation'}, DATA), 'the dissolved confirmation does not revive the other\'s annulment'),
    ('Num 30:7 / Sifrei 153:7; Shevuot 20a:4-9; Lev 5:4 by CALL — the utterance is an oath', lambda: the_betrothed({'ask': 'utterance_is_oath'}, DATA), 'the utterance of her lips = an oath — Leviticus 5:4 by call'),
    ('Mishnah Nedarim 10:7; Sifrei 153:10; Nedarim 75a:6 — annulling in advance', lambda: the_betrothed({'ask': 'annul_in_advance'}, DATA), '"all vows you will vow are annulled" — nothing (the Rabbis)'),
    ('Num 30:14 / Sifrei 153:10 — what came to confirmation came to annulment', lambda: the_betrothed({'ask': 'confirmation_and_annulment_reach'}, DATA), 'the two verbs one reach'),
    ('Nedarim 71b:2-72a:8 — divorce as silence or confirmation (unresolved)', lambda: the_betrothed({'ask': 'divorce_as'}, DATA), 'unresolved — the machine writes nothing at a divorce'),
    ('Mishnah Nedarim 10:5; Nedarim 73b:5 — the sustained betrothed', lambda: the_betrothed({'ask': 'sustained_betrothed'}, DATA), 'the sustained betrothed — R. Eliezer\'s arm recorded; the Rabbis rule'),
    ('Mishnah Nedarim 10:6; Nedarim 74a-75a — the levirate widow', lambda: the_betrothed({'ask': 'levirate_widow'}, DATA), 'the levirate widow — R. Akiva: no annulment'),
    ('Num 30:9 / Nedarim 73a:5-7 — two wives (NS.sotah by reference)', lambda: the_betrothed({'ask': 'two_wives'}, DATA), 'one wife at a time'),
    ('Mishnah Nedarim 10:3 — betrothed a hundred times the same day', lambda: the_betrothed({'ask': 'same_day_hundred'}, DATA), 'the last husband and the father annul'),
    # F4 — the widow and the divorcee
    ('Num 30:10 / Sifrei 154:1; Ketubot 49a:2 — from marriage', lambda: the_widow({'ask': 'from_marriage'}, DATA), 'no annuller — the vow stands'),
    ('Sifrei 154:1; Mishnah Nedarim 11:10; Nedarim 89b:2 — the orphan in her father\'s lifetime', lambda: the_widow({'ask': 'orphan_in_fathers_lifetime'}, DATA), 'the orphan in her father\'s lifetime — her vows stand'),
    ('Mishnah Nedarim 11:9 — vowed in widowhood, then married', lambda: the_widow({'ask': 'remarried', 'when': 'before'}, DATA), 'vowed in widowhood — the new husband annuls nothing'),
    ('Num 30:11 / Sifrei 154:1 — vowed in his house', lambda: the_widow({'ask': 'remarried', 'when': 'after'}, DATA), 'vowed in his house — the husband annuls'),
    ('Nedarim 89a:2-5 — the vow\'s timing (R. Yishmael / R. Akiva)', lambda: the_widow({'ask': 'vow_timing'}, DATA), 'the authority at the vow\'s making — the marriage-hook the disputed arm'),
    ('Mishnah Nedarim 11:9; Yevamot 87a:7 — once out one hour', lambda: the_widow({'ask': 'once_out_one_hour'}, DATA), 'out one hour — the earlier vows beyond him'),
    ('Lev 22:13 by CALL; Yevamot 87a:6 — the priest\'s daughter\'s pair of words', lambda: the_widow({'ask': 'priests_daughter_pair'}, DATA), 'the pair of words shared — the return is for terumah, not for vows'),
    ('Mishnah Nedarim 10:6 — awaiting the brother-in-law', lambda: the_widow({'ask': 'levirate'}, DATA), 'awaiting the brother-in-law — her vow stands'),
    # F5 — the married woman
    ('Num 30:11 / Nedarim 67b:1 — vowed before the marriage', lambda: the_wife({'ask': 'in_husbands_house', 'when': 'before'}, DATA), 'vowed before the marriage — beyond him'),
    ('Num 30:11 / Sifrei 154:1 — vowed in his house', lambda: the_wife({'ask': 'in_husbands_house', 'when': 'after'}, DATA), 'vowed in his house — he annuls'),
    ('Mishnah Nedarim 10:4; Nedarim 72b:4 — the scholars\' practice', lambda: the_wife({'ask': 'scholars_practice'}, DATA), 'the advance annulment a conditional on the hearing'),
    ('Num 30:12, 30:15 / Sifrei 154:2, 156:1; Nedarim 79a:5 — the two silences', lambda: the_wife({'ask': 'two_silences'}, DATA), 'both silences confirm at the day\'s end'),
    ('Nedarim 77b:5 — "you did well"', lambda: the_wife({'ask': 'confirming_words', 'said': 'well_done'}, DATA), 'confirmed by his words at once'),
    ('Nedarim 77b:5 — "I do not want you to vow"', lambda: the_wife({'ask': 'confirming_words', 'said': 'do_not_want'}, DATA), 'nothing said — the day runs'),
    ('Sifrei 154:2 — leave to annul all the day', lambda: the_wife({'ask': 'all_the_day'}, DATA), 'leave to annul all the day'),
    ('Num 30:13 / Sifrei 154:3 — the caretaker excluded', lambda: the_wife({'ask': 'caretaker_excluded'}, DATA), 'the caretaker excluded — R. Yonatan\'s agent recorded'),
    ('Nedarim 69a:4, 79a:3 — the sage over the confirmation', lambda: the_wife({'ask': 'sage_over_confirmation'}, DATA), 'the confirmation reopened by the sage; the annulment never'),
    ('Nedarim 69b:3 — confirmed and annulled at once', lambda: the_wife({'ask': 'confirmed_and_annulled', 'form': 'at_once'}, DATA), 'nothing — the two ops exclusive'),
    ('Nedarim 69b:1-2 — confirmed on condition the annulment holds', lambda: the_wife({'ask': 'confirmed_and_annulled', 'form': 'conditioned'}, DATA), 'annulled — the condition carries it'),
    ('Mishnah Nedarim 11:5; Nedarim 87a:3 — the mistaken annulment', lambda: the_wife({'ask': 'mistaken_annulment'}, DATA), 'the mistaken annulment void'),
    ('Nedarim 87a:5-8 — within the time of a short phrase', lambda: the_wife({'ask': 'short_phrase'}, DATA), 'the retraction window of a short phrase — the vow and its annulment inside it'),
    ('Mishnah Nazir 4:1; NS by CALL — her "and I" after his', lambda: the_wife({'ask': 'her_and_i', 'who_first': 'husband'}, DATA), 'her "and I" annulled'),
    ('Mishnah Nazir 4:1 — his "and I" after hers', lambda: the_wife({'ask': 'her_and_i', 'who_first': 'wife'}, DATA), 'his "and I" — he cannot annul hers'),
    ('Num 30:13 / Sifrei 154:3; Nazir 23a:3 — the forgiveness', lambda: the_wife({'ask': 'forgiveness_wife'}, DATA), 'forgiven — annulled unknown to her'),
    ('Nedarim 89b:4-5, 90a:2 — annulled before it takes effect', lambda: the_wife({'ask': 'annul_before_effect'}, DATA), 'annulled before it takes effect — the Rabbis'),
    ('Nedarim 73b:5 — every woman vows on her husband\'s consent', lambda: the_wife({'ask': 'consent_rationale'}, DATA), 'the husband\'s power explained by the sustenance'),
    ('Gittin 85a:22, 73b:16 — divorced except the vows', lambda: the_wife({'ask': 'divorce_except_vows'}, DATA), 'the power a marriage component — the severance question open'),
    # F6 — the affliction oath and the day
    ('Num 30:14, 30:17 / Sifrei 155:1; Nedarim 81b:2 — the filter: affliction', lambda: the_affliction_oath({'ask': 'the_filter', 'content_class': 'affliction'}, DATA), 'annulled — affliction or between them'),
    ('Nedarim 79b:2 — the filter: between him and her', lambda: the_affliction_oath({'ask': 'the_filter', 'content_class': 'between'}, DATA), 'annulled — affliction or between them'),
    ('Mishnah Nedarim 11:3-4 — the filter: neither', lambda: the_affliction_oath({'ask': 'the_filter', 'content_class': 'other'}, DATA), 'not annulled — neither affliction nor between them'),
    ('Mishnah Nedarim 11:2 — the produce of the world', lambda: the_affliction_oath({'ask': 'affliction_scope', 'what': 'world'}, DATA), 'annulled'),
    ('Mishnah Nedarim 11:2 — the produce of this country', lambda: the_affliction_oath({'ask': 'affliction_scope', 'what': 'country'}, DATA), 'not annulled — he supplies from elsewhere'),
    ('Mishnah Nedarim 11:2 — this storekeeper, his sole supplier', lambda: the_affliction_oath({'ask': 'affliction_scope', 'what': 'sole_storekeeper'}, DATA), 'annulled'),
    ('Mishnah Nedarim 11:1; Nedarim 81a:10, 81b:2-3 — the bathe / adorn vows', lambda: the_affliction_oath({'ask': 'bathing'}, DATA), 'the bathe / adorn vows annulled — as affliction or as between them'),
    ('Nedarim 80b:6; Lev 23:27 by CALL — Rava\'s two afflictions', lambda: the_affliction_oath({'ask': 'two_afflictions'}, DATA), 'one root, two senses — the vow\'s affliction is what leads to it'),
    ('Nedarim 79b:5, 82a:1 — the two reaches', lambda: the_affliction_oath({'ask': 'annulment_reach'}, DATA), 'two reaches — for others (affliction), for himself (between them)'),
    ('Mishnah Nedarim 11:4; Nedarim 81b:4, 85a:9 — the void vow on an owed duty', lambda: the_affliction_oath({'ask': 'void_vow_owed_duty'}, DATA), 'no vow — she owes the work; annulled anyway for the excess or the divorce'),
    ('Nedarim 81b:8 — we do not feed a person what is forbidden to him', lambda: the_affliction_oath({'ask': 'we_do_not_feed'}, DATA), 'the self-prohibition annulled — the owed duty does not lift it'),
    ('Mishnah Nedarim 11:12; Nedarim 82a:1 — removed from the Jews', lambda: the_affliction_oath({'ask': 'removed_from_the_jews'}, DATA), 'his part annulled — the between-them reach'),
    ('Sifrei 155:1 — the father\'s reach', lambda: the_affliction_oath({'ask': 'fathers_reach'}, DATA), 'the father\'s reach by the likening'),
    ('Mishnah Nedarim 11:6; Nedarim 87a:10 — confirmed for the figs', lambda: the_affliction_oath({'ask': 'partial_annulment', 'act': 'confirm_part'}, DATA), 'confirmed for a part — all confirmed'),
    ('Mishnah Nedarim 11:6; Nedarim 87b:1-2 — annulled for the figs', lambda: the_affliction_oath({'ask': 'partial_annulment', 'act': 'annul_part'}, DATA), 'annulled for a part — not annulled till the whole (R. Yishmael)'),
    ('Nedarim 82b:2-3 — the two loaves', lambda: the_affliction_oath({'ask': 'two_loaves'}, DATA), 'the mixed vow — R. Yochanan: the afflicting loaf alone'),
    ('Nedarim 83a:3-6; NS by CALL — the naziriteship annulled whole', lambda: the_affliction_oath({'ask': 'nazirite_whole'}, DATA), 'her naziriteship annulled whole'),
    ('Sifrei 156:1; Nedarim 76b:4-8; the calendar row — the deadline', lambda: the_affliction_oath({'ask': 'the_deadline'}, DATA), 'to nightfall — the timer due the hearing day + 1; the twenty-four hours recorded'),
    ('Mishnah Nedarim 10:8 — the leniency and the stringency', lambda: the_affliction_oath({'ask': 'day_leniency_stringency'}, DATA), 'the day ends at dark — a night and a day, or an hour'),
    ('Nedarim 78b:4-79a:9 — the silence to vex', lambda: the_affliction_oath({'ask': 'silence_to_vex'}, DATA), 'the vexing silence confirms at nightfall — the timer fires whatever the intent'),
    ('Mishnah Shabbat 24:5; Nedarim 77a:4, 77b:6 — the annulment on the Sabbath', lambda: the_affliction_oath({'ask': 'annul_on_sabbath'}, DATA), 'annulled on the Sabbath — "take and eat"'),
    ('Mishnah Nedarim 11:7 — the day he learned', lambda: the_affliction_oath({'ask': 'day_of_learning'}, DATA), 'the day he learned — a second hearing day'),
    ('Num 30:16 / Sifrei 156:2; Nedarim 79a:4 — after his hearing', lambda: the_affliction_oath({'ask': 'after_his_hearing'}, DATA), 'annulled after the day — the vow stands, the husband bears her iniquity'),
    ('Num 30:16, 5:31 by CALL; Nedarim 83a:1 — she is clear', lambda: the_affliction_oath({'ask': 'she_is_clear'}, DATA), 'she is clear — the iniquity his'),
    ('Sifrei 156:2; Sanhedrin 100a:18; Yoma 76a:7 — the measure of good', lambda: the_affliction_oath({'ask': 'measure_of_good'}, DATA), 'the a-fortiori from the two measures — the ratio a recorded parameter'),
    ('Shevuot 27a:6; Lev 5:4 by CALL — the oath to harm himself', lambda: the_affliction_oath({'ask': 'oath_to_harm_himself'}, DATA), 'the affliction oath the oath to harm oneself — bound'),
    ('Num 30:14 / Nedarim 80b:3-4 — vows and oaths one class', lambda: the_affliction_oath({'ask': 'vows_and_oaths_one_class'}, DATA), 'vows and oaths one class for the annulment'),
    # F7 — the statutes
    ('Num 30:17 / Sifrei 156:3; Nedarim 68a:1 — the likening both ways', lambda: the_statutes({'ask': 'likening_both_ways'}, DATA), 'the footer likens both ways — the engine of the chapter'),
    ('Num 30:17 / Sifrei 156:3; Nedarim 70a:7 — in her youth, her father\'s house', lambda: the_statutes({'ask': 'in_her_youth_her_fathers_house'}, DATA), 'the father\'s bound; the husband\'s reach'),
    ('Ketubot 40b:4; Kiddushin 3b:7 — the father\'s gains', lambda: the_statutes({'ask': 'fathers_gains'}, DATA), 'the clause generalized — labeled'),
    ('Num 30:1 / THE REGISTER GATE — the receipt\'s second form', lambda: the_statutes({'ask': 'the_receipt'}, DATA), 'the receipt that closes a speech — in the census by the finder\'s second form'),
    ('Num 30:17 / THE REGISTER GATE — the footer\'s block', lambda: the_statutes({'ask': 'the_register_gate'}, DATA), 'the footer DAEMONS — law_vows joined its block'),
    ('Num 30:3-16 — the case structure (computed)', lambda: the_statutes({'ask': 'case_structure'}, DATA), 'two when, seven and-if — the draft\'s nine rows'),
    ('Num 30:6-16 — the clock words (computed)', lambda: the_statutes({'ask': 'clock_words'}, DATA), 'the clock the chapter\'s only number'),
    ('Num 30:3-16 — the doubled verbs (computed)', lambda: the_statutes({'ask': 'doubled_verbs'}, DATA), 'five doubled verbs — every one read by the shelf as law'),
    ('Num 30:2-17 — the tape\'s one line', lambda: the_statutes({'ask': 'the_line'}, DATA), 'the statutes of vows commanded — one write, no timer, no close'),
    ('THE LOOP step 3 — installed_by for a law in Moses\' voice', lambda: the_statutes({'ask': 'installed_by'}, DATA), 'installed_by boot — a statute relayed in Moses\' voice, the class named'),
    ('Bava Batra 120b:1; Nedarim 78a:2 — for all generations', lambda: the_statutes({'ask': 'all_generations'}, DATA), 'for all generations — the relay not case-bound'),
    ('Nedarim 78a:9-78b:2 — the chapter\'s placement', lambda: the_statutes({'ask': 'placement_after_the_calendar'}, DATA), 'the chapter\'s placement read as law — next to the calendar, not of it'),
    ('Num 30:3, 30:4, 30:6, 30:15 — two kinds of ki (computed)', lambda: the_statutes({'ask': 'two_kinds_of_ki'}, DATA), 'one particle, two jobs — the parse decides'),
    # THE INK, computed
    ('THE PARSER — no cardinal, no ordinal; the three oath-tokens starred', lambda: (([n for n in NUMBERS.values() if n], [o for o in ORDINALS.values() if o], STARRED), [FX.NONE], [('INK', 'Num 30:1-17 — the parser')]), ([], [], [(3, 'שבעה*'), (11, 'בשבעה*'), (14, 'שבעת*')])),
    ('THE CASE STRUCTURE — two when, seven and-if, the two other ki (computed)', lambda: ((WHEN, AND_IF, KI_SEATS), [FX.NONE], [('INK', 'Num 30:3-16 — computed on the first words')]), ([3, 4], [6, 7, 9, 11, 13, 15, 16], [(3, 1), (4, 1), (6, 18), (15, 20)])),
    ('THE CLOCK WORDS — on the day of his hearing, from day to day, after his hearing (computed)', lambda: ((DAY_OF_HEARING, DAY_TO_DAY, AFTER_HEARING), [FX.NONE], [('INK', 'the whole DB')]), (['Num 30:6', 'Num 30:8', 'Num 30:13', 'Num 30:15'], ['1Chr 16:23', 'Num 30:15'], ['Num 30:16'])),
    ('THE FRAMES — this is the thing (8), the heads of the tribes (3), these are the statutes (3), the receipt\'s second form (7)', lambda: ((len(THIS_IS), THIS_IS[-2:], HEADS, FOOTER, len(RECEIPT2), RECEIPT2[-1]), [FX.NONE], [('INK', 'the whole DB')]), (8, ['Num 30:2', 'Num 36:6'], ['1Kgs 8:1', '2Chr 5:2', 'Num 30:2'], ['Deut 12:1', 'Lev 26:46', 'Num 30:17'], 7, 'Num 30:1')),
    ('THE DOUBLED VERBS — annul (2 seats), be (2), silent (1), swear (1)', lambda: ((ANNUL_ANNUL, BE_BE, SILENT_SILENT, SWEAR_OATH), [FX.NONE], [('INK', 'the whole DB')]), (['Num 30:13', 'Num 30:16'], ['Jer 15:18', 'Num 30:7'], ['Num 30:15'], ['Num 30:3'])),
    ('THE PERSONS AND THE PAIRS — her husband 9, her father 6; the widow\'s pair 3; the utterance 2; in her youth 2', lambda: ((HUSBAND_TOKENS, FATHER_TOKENS, WIDOW_DIVORCEE, UTTERANCE, IN_HER_YOUTH), [FX.NONE], [('INK', 'Num 30 and the whole DB')]), (9, 6, ['Lev 21:14', 'Lev 22:13', 'Num 30:10'], ['Num 30:7', 'Num 30:9'], ['Num 30:4', 'Num 30:17'])),
    ('THE FORGIVENESS AND THE INIQUITY — three seats; one seat; the frame verbs Moses\'', lambda: ((FORGIVE, BEAR_HER, FRAME_VERBS, CONFIRM_ANNUL_IT), [FX.NONE], [('INK', 'the whole DB')]), (['Num 30:6', 'Num 30:9', 'Num 30:13'], ['Num 30:16'], [(1, 'ויאמר'), (2, 'וידבר')], ('יקימנו', 'יפרנו'))),
    # THE CALLEES
    ('THE NASO RUNNER — the nazirite\'s vow-form and the sotah\'s 5:31 (by CALL)', lambda: ((NAZ_SUB[0], NAZ_PART[0], SOTAH_CLEAN[0], SOTAH_UNCLEAN[0][:19]), [FX.NONE], [('MOVE', 'CALLED cold_run_naso')]), ('binds (nazir lehazir)', 'a full nazirite', 'tested', 'the waters do not ')),
    ('THE LEVITICUS 5 RUNNER — the utterance oath\'s option template (by CALL)', lambda: ((OATH_OPTION[0][:7], OATH_NO_OPTION[0]), [FX.NONE], [('MOVE', 'CALLED cold_run_vayikra5')]), ('CONFESS', 'exempt')),
    ('THE PRIESTHOOD RUNNER — the priest\'s daughter\'s return (by CALL)', lambda: ((PR_RETURN['v']['widow_and_divorcee'], PR_TABLE['v']), [FX.NONE], [('MOVE', 'CALLED cold_run_priesthood')]), ('both_written_both_need_no_seed', 'terumah_returns')),
    ('THE MUSAFIM RUNNER — the vow_deadline row (by CALL)', lambda: ((MU_DEADLINE[0], MU_ROW['value'], sorted(MU_ROW['settings'])), [FX.NONE], [('MOVE', 'CALLED cold_run_musafim')]), ('three festivals in any order — the first tanna', 'three_festivals_any_order', ['by_sukkot', 'one_festival', 'three_festivals_any_order', 'three_in_order'])),
    ('THE MOADIM RUNNER — the affliction list (by CALL)', lambda: (MO_AFFLICTION, [FX.NONE], [('MOVE', 'CALLED cold_run_moadim')]), 'eating_drinking_washing_anointing_sandals_relations'),
    ('THE CALENDAR ROW — vow_annulment_window (the third registry)', lambda: ((WINDOW, sorted(CAL_ROW['settings']), CAL_ROW['channel']), [FX.NONE], [('DATA', 'calendar_parameters.yaml')]), ('to_nightfall', ['to_nightfall', 'twenty_four_hours'], 'received')),
    # THE WRAP: the scene on the world engine
    ('THE SCENE on the world engine — THE STATE MACHINE\'s persons and the exam\'s through the ten case kinds; the timers set, fired and cancelled (predicted before the run)',
     lambda: (SCENE, [FX.NONE], [('INK', 'Num 30:1-17 — the recorded rows replayed')]), SCENE_PREDICTED),
    ('THE NARRATIVE on the world engine — the one line; one write, no timer (predicted before the run)',
     lambda: (NARRATIVE, [FX.NONE], [('INK', 'Num 30:2-17 — the one line')]), (1, 0, 1, (6, 1))),
]

if __name__ == '__main__':
    ok = 0
    frac = {'INK': 0, 'MOVE': 0, 'DATA': 0, 'HYP': 0}
    used_effects = []
    print()
    for label, fn, want in CASES:
        got, effects, prov = fn()
        hit = got == want
        ok += hit
        kinds = [k for k, _ in prov]
        cls = 'HYP' if 'HYP' in kinds else ('INK' if all(k == 'INK' for k in kinds) else ('MOVE' if 'MOVE' in kinds else 'DATA'))
        frac[cls] += 1
        print('%s  [%s]  %s' % ('PASS' if hit else 'MISS', cls, label))
        if not hit:
            print('      expected: %s' % (want,))
            print('      got     : %s' % (got,))
        used_effects += effects
        for line in FX.render(effects):
            print('        ->%s' % line)
    print()
    print('WATCH COVERAGE (the wrap):')
    _W.print_coverage()
    print('MATRIX: %d/%d cells match the answer sheet' % (ok, len(CASES)))
    tot = len(CASES)
    print('FRACTIONS: pure ink %d/%d (%.0f%%) · named moves %d/%d (%.0f%%) · data %d/%d (%.0f%%) · hypotheses %d/%d (the H class, counted apart — never as compiled)' %
          (frac['INK'], tot, 100.0 * frac['INK'] / tot, frac['MOVE'], tot, 100.0 * frac['MOVE'] / tot, frac['DATA'], tot, 100.0 * frac['DATA'] / tot, frac['HYP'], tot))
    ops = FX.summarize(used_effects)
    print('LEDGER OPS this span writes:', ', '.join('%s x%d' % kv for kv in sorted(ops.items())))
    print('THE INK: numbers %s; starred %s; when %s; and-if %s; the clock words %s / %s / %s; the doubled verbs %s' % ([n for n in NUMBERS.values() if n], STARRED, WHEN, AND_IF, DAY_OF_HEARING, DAY_TO_DAY, AFTER_HEARING, DOUBLED))
    print('THE STATE MACHINE on the bench: %s; the timers (set, fired, cancelled, pending) %s; the exam persons %s; entities %d' % SCENE)
    print('THE NARRATIVE: %s' % (NARRATIVE,))
    print('THE CALENDAR ROW: vow_annulment_window = %s (settings %s)' % (WINDOW, sorted(CAL_ROW['settings'])))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value']) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE COMPILE OF THE VOWS: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)

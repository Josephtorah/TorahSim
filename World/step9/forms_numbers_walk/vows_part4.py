

# ===== F5: THE MARRIED WOMAN (Num 30:11-13) ====================================================================
def the_wife(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'in_husbands_house':
        when = case['when']
        ink('30:11', '"and if in her husband\'s house she vowed" — "her husband\'s house" %s (computed); the married (30:7 having taken the betrothed — Sifrei 154:1)' % HUSBANDS_HOUSE)
        move('Nedarim 67b:1, 67b:6; Mishnah Nedarim 10:4', 'the husband annuls only vows made AFTER the marriage — not those before')
        return out('vowed before the marriage — beyond him' if when == 'before' else 'vowed in his house — he annuls', ['vow_bound'] if when == 'before' else ['vow_annulled'])
    if ask == 'scholars_practice':
        move('Mishnah Nedarim 10:4 (72b:1); 72b:4', 'the father before she leaves and the husband before she enters annul her vows in advance — "when I hear it": the practice prompts her to tell')
        return out('the advance annulment a conditional on the hearing', ['accepted'])
    if ask == 'two_silences':
        ink('30:12, 30:15', '"and was silent to her" (the single form at 30:5, 8, 12) against "silent, he is silent ... from day to day" (30:15 — %s)' % SILENT_SILENT)
        move('Sifrei 154:2, 156:1; Nedarim 79a:4-5, 79a:6', 'the silence to CONFIRM and the silence to VEX — both confirm ("superfluous verses are written about silence"); R. Chanina refuted')
        return out('both silences confirm at the day\'s end', ['vow_confirmed'])
    if ask == 'confirming_words':
        said = case['said']
        move('Nedarim 77b:5', '"you did well", "there is none like you", "had you not vowed I would have made you" — CONFIRMED; "I do not want you to vow", "this is no vow" — nothing')
        return out('confirmed by his words at once' if said == 'well_done' else 'nothing said — the day runs', ['vow_confirmed'] if said == 'well_done' else ['accepted'])
    if ask == 'all_the_day':
        move('Sifrei 154:2 (the Hebrew\'s close)', '"leave to annul all the day" — the married woman\'s verse')
        return out('leave to annul all the day', ['vow_annulled'])
    if ask == 'caretaker_excluded':
        ink('30:13', '"all that proceeds from her lips ... shall not stand" — to exclude the caretaker (Sifrei 154:3\'s lemma); "her husband has annulled them" — his act')
        dat('the row annul_by_messenger = %s' % data['annul_by_messenger']['value'])
        return out('the caretaker excluded — R. Yonatan\'s agent recorded', ['accepted'])
    if ask == 'sage_over_confirmation':
        move('Nedarim 69a:4, 79a:3 (R. Yochanan)', 'a sage dissolves a CONFIRMATION, not an ANNULMENT')
        dat('the row confirmation_dissolved = %s' % data['confirmation_dissolved']['value'])
        return out('the confirmation reopened by the sage; the annulment never', ['accepted'])
    if ask == 'confirmed_and_annulled':
        form = case['form']
        move('Nedarim 69b:3 (Rabba); 69b:1-2', '"confirmed and annulled" at once — nothing (what cannot be done in sequence is not done at once); "confirmed on condition the annulment holds" — annulled')
        return out('annulled — the condition carries it' if form == 'conditioned' else 'nothing — the two ops exclusive', ['vow_annulled'] if form == 'conditioned' else ['accepted'])
    if ask == 'mistaken_annulment':
        move('Mishnah Nedarim 11:5 (86b:4); 86b:5; 87a:3', 'the wife thought the daughter, the naziriteship thought an offering — he annuls AGAIN; a specified wrong report voids it')
        return out('the mistaken annulment void', ['accepted'])
    if ask == 'short_phrase':
        move('Nedarim 87a:5, 87a:8 (Rav Ashi; the halakha, the ruling)', 'within the time of a short phrase the act is open — except the blasphemer, the idolater, the betrother, the divorcer')
        return out('the retraction window of a short phrase — the vow and its annulment inside it', ['accepted'])
    if ask == 'her_and_i':
        who = case['who_first']
        move('CALLED cold_run_naso.nazirite(vow_form) -> %s [IMPORT, live]' % NAZ_SUB[0], 'the nazirite\'s vow annullable like a vow (Nedarim 3a:7)')
        move('Mishnah Nazir 4:1 (Nazir 20b:4)', 'he said "I am a nazirite" and she "and I" — he annuls hers, his stands; she first and he "and I" — he cannot (he would annul his own)')
        return out('her "and I" annulled' if who == 'husband' else 'his "and I" — he cannot annul hers', ['vow_annulled'] if who == 'husband' else ['vow_bound'])
    if ask == 'forgiveness_wife':
        ink('30:13', '"her husband has annulled them, and the LORD will forgive her" — the clause\'s third seat')
        move('Sifrei 154:3; Nazir 23a:3', 'as above — the woman who did not know')
        return out('forgiven — annulled unknown to her', ['vow_annulled'])
    if ask == 'annul_before_effect':
        move('Nedarim 89b:4-5 (R. Natan / the Rabbis); 90a:2', 'a conditional vow not yet in effect — R. Natan: he cannot annul; the Rabbis: he can ("He annuls the thoughts of the crafty")')
        dat('the row annul_before_effect = %s' % data['annul_before_effect']['value'])
        return out('annulled before it takes effect — the Rabbis', ['accepted'])
    if ask == 'consent_rationale':
        move('Nedarim 73b:5 (Rav Pinchas in Rava\'s name); 74a:9', 'EVERY WOMAN WHO VOWS, VOWS ON HER HUSBAND\'S CONSENT — he sustains her')
        return out('the husband\'s power explained by the sustenance', ['accepted'])
    if ask == 'divorce_except_vows':
        move('Gittin 85a:22; 73b:16', '"divorced except the annulment of your vows" — is the power intrinsic to marriage? a dilemma; the conditional bill keeps his power in the interval')
        return out('the power a marriage component — the severance question open', ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F6: THE AFFLICTION OATH AND THE DAY (Num 30:14-16) ===================================================
def the_affliction_oath(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_filter':
        cls = case['content_class']
        ink('30:14, 30:17', '"every vow and every oath of binding TO AFFLICT A SOUL" (%s) restricts 30:9\'s "the vow upon her"; "between a man and his wife" (30:17, %s) adds the vows that touch him' % (AFFLICT, BETWEEN_MAN))
        move('Sifrei 155:1; Nedarim 79b:2; the baraita 81b:2', 'THE FOUR-CELL TABLE — affliction vows annulled whether between them or between her and others; non-affliction vows annulled only between him and her')
        move('Mishnah Nedarim 11:3-4', '"the property of people is konam to me" — not annulled; "I will not make for my father" — not; "for my father if I make for you" — annulled (11:11)')
        return out('annulled — affliction or between them' if cls in ('affliction', 'between') else 'not annulled — neither affliction nor between them', ['vow_annulled'] if cls in ('affliction', 'between') else ['vow_bound'])
    if ask == 'affliction_scope':
        what = case['what']
        move('Mishnah Nedarim 11:2 (79b:1); Sifrei 155:1 (R. Yonatan)', 'the produce of the WORLD — annulled; of this COUNTRY — not (he brings from another); of this STOREKEEPER — not, unless his sustenance is from him alone')
        move('Nedarim 82a:3, 82b:1 (Shmuel; Rav Huna)', 'the whole chapter R. Yosei\'s; Shmuel rules as the Rabbis — every affliction vow but one wholly between her and another')
        dat('the row affliction_scope = %s' % data['affliction_scope']['value'])
        return out('annulled' if what in ('world', 'sole_storekeeper') else 'not annulled — he supplies from elsewhere', ['vow_annulled'] if what in ('world', 'sole_storekeeper') else ['vow_bound'])
    if ask == 'bathing':
        move('Mishnah Nedarim 11:1; 81a:10 (Rav Adda b. Ahava / Rav Huna); 81b:2-3', '"if I bathe / do not bathe, adorn / do not adorn" — affliction (the Rabbis); not (R. Yosei) — annulled as between him and her (Rav Adda; the baraita: painting the eyes, rouge)')
        dat('the row affliction_scope = %s' % data['affliction_scope']['value'])
        return out('the bathe / adorn vows annulled — as affliction or as between them', ['vow_annulled'])
    if ask == 'two_afflictions':
        ink('30:14', '"to afflict a soul" — the infinitive\'s two Bible seats, Pharaoh\'s (Exod 10:3) and this (computed at the reading)')
        move('CALLED cold_run_moadim.yom_kippur() -> affliction_list %s [IMPORT, live]' % MO_AFFLICTION, 'Lev 23:27\'s afflictions — the five from the five mentions (Yoma 76a:11, 29:7 among them)')
        move('Nedarim 80b:6 (Rava)', 'Yom Kippur\'s affliction is felt NOW; the vows\' is what LEADS to affliction — one root, two senses read from each context')
        return out('one root, two senses — the vow\'s affliction is what leads to it', ['accepted'])
    if ask == 'annulment_reach':
        move('Nedarim 79b:5; 82a:1; 84a:2', 'affliction vows annulled for himself AND for others; between-them vows for himself only — "I am removed from the Jews": his part annulled, forbidden to all if divorced')
        dat('the row annulment_reach = %s' % data['annulment_reach']['value'])
        return out('two reaches — for others (affliction), for himself (between them)', ['accepted'])
    if ask == 'void_vow_owed_duty':
        move('Mishnah Nedarim 11:4 (85a:6); 81b:4', '"I will not make anything for YOU", "I will not make your bed" — no need to annul: it is VOID, she owes it')
        move('Mishnah Nedarim 11:4 (R. Akiva; R. Yochanan b. Nuri); Shmuel 85a:9; Rav Ashi 86b:1-2', 'annul it anyway — the excess (R. Akiva), lest he divorce her (b. Nuri — the halakha, the ruling); konamot break the lien')
        return out('no vow — she owes the work; annulled anyway for the excess or the divorce', ['exempt'])
    if ask == 'we_do_not_feed':
        move('Nedarim 81b:7-8 (Rav Kahana)', '"MY intercourse forbidden to you" — he compels her; "YOUR intercourse forbidden to me" — he must annul: we do not feed a person what is forbidden to him')
        return out('the self-prohibition annulled — the owed duty does not lift it', ['vow_annulled'])
    if ask == 'removed_from_the_jews':
        move('Mishnah Nedarim 11:12 (90b:5-6); 82a:1', '"I am removed from the Jews" — he annuls HIS PART; she is removed from all others if divorced — between him and her')
        return out('his part annulled — the between-them reach', ['vow_annulled'])
    if ask == 'fathers_reach':
        move('Sifrei 155:1', '"I reasoned and reversed" — the father likened to the husband by 30:17 (the third row ending on the footer)')
        dat('the row fathers_scope = %s' % data['fathers_scope']['value'])
        return out('the father\'s reach by the likening', ['accepted'])
    if ask == 'partial_annulment':
        act = case['act']
        ink('30:14', '"her husband shall confirm IT ... annul IT" — the two verbs with the one suffix %s (computed)' % (CONFIRM_ANNUL_IT,))
        move('Sifrei 155:1; Mishnah Nedarim 11:6 (87a:9); 87a:10; 87b:1-2', 'R. Yishmael: "figs and grapes" — confirmed for the figs, ALL confirmed; annulled for the figs, NOT till the grapes; R. Akiva: yakim MIMMENNU — a part annuls the whole; the Rabbis: no more than he annulled')
        dat('the row partial_annulment = %s' % data['partial_annulment']['value'])
        return out('confirmed for a part — all confirmed' if act == 'confirm_part' else 'annulled for a part — not annulled till the whole (R. Yishmael)', ['vow_confirmed'] if act == 'confirm_part' else ['vow_bound'])
    if ask == 'two_loaves':
        move('Nedarim 82b:2-3 (Shmuel / R. Yochanan)', 'one fine loaf (affliction) and one poor — Shmuel: both annulled; R. Yochanan: the afflicting one only')
        return out('the mixed vow — R. Yochanan: the afflicting loaf alone', ['accepted'])
    if ask == 'nazirite_whole':
        move('CALLED cold_run_naso.nazirite(vow_form, partial) -> %s [IMPORT, live]' % NAZ_PART[0], 'one prohibition named — a full nazirite')
        move('Nedarim 83a:3-6 (Rav Yosef; Abaye)', 'NAZIRITESHIP TAKES NO PARTIAL EFFECT — the annulment cancels the whole; a bird sin offering on the doubt')
        return out('her naziriteship annulled whole', ['vow_annulled'])
    if ask == 'the_deadline':
        ink('30:13, 30:15', '"on the day that he hears them" (%d seats, all here) against "from day to day" (%s)' % (len(DAY_OF_HEARING), DAY_TO_DAY))
        move('Sifrei 156:1; Nedarim 76b:4-8; Mishnah Nedarim 10:8', 'the whole day till dark (the first tanna) against the pair\'s twenty-four hours (R. Shimon ben Yochai in the Sifrei); each arm reads both clauses; R. Yehoshua b. Levi: the halakha (the ruling) is NOT as that pair')
        dat('the calendar row vow_annulment_window = %s (the other setting %s recorded)' % (WINDOW, [k for k in CAL_ROW['settings'] if k != WINDOW]))
        return out('to nightfall — the timer due the hearing day + 1; the twenty-four hours recorded', ['vow_confirmed'])
    if ask == 'day_leniency_stringency':
        move('Mishnah Nedarim 10:8 (76b:2-3)', 'vowed Friday night — annulled through the Sabbath till dark (the leniency); vowed near dark — till dark only (the stringency)')
        return out('the day ends at dark — a night and a day, or an hour', ['vow_confirmed'])
    if ask == 'silence_to_vex':
        move('Nedarim 78b:4-79a:9', 'R. Chanina: the vexing silence annuls ten days later — REFUTED three times (the deaths baraita; the near-dark vow; the day of learning)')
        return out('the vexing silence confirms at nightfall — the timer fires whatever the intent', ['vow_confirmed'])
    if ask == 'annul_on_sabbath':
        move('Mishnah Shabbat 24:5 (157a:5); Nedarim 77a:4; 77b:6', 'he annuls on the Sabbath even not for its need (by the whole-day arm); the formula "take and eat" with the heart\'s annulment')
        dat('the row annul_on_sabbath = %s' % data['annul_on_sabbath']['value'])
        return out('annulled on the Sabbath — "take and eat"', ['vow_annulled'])
    if ask == 'day_of_learning':
        move('Mishnah Nedarim 11:7 (87b:4)', '"I did not know there are annullers" — he annuls on the day he LEARNED; "I did not know this is a vow" — R. Meir no, the Rabbis yes')
        dat('the row hearing_of_the_law = %s' % data['hearing_of_the_law']['value'])
        return out('the day he learned — a second hearing day', ['vow_annulled'])
    if ask == 'after_his_hearing':
        ink('30:16', '"and if he annul, he annuls them AFTER HIS HEARING, then he shall bear her iniquity" — "after his hearing" %s; "annul, he annuls" %s (computed)' % (AFTER_HEARING, ANNUL_ANNUL))
        move('Sifrei 156:2', '"after his hearing" = after his CONFIRMING (freed by 30:15\'s neighbor) — he enters in her place for the sin')
        move('Nedarim 79a:4-5; Mishnah Nedarim 10:7', 'the husband who annuls a confirmed vow, so that she breaks it relying on him — he bears her iniquity')
        return out('annulled after the day — the vow stands, the husband bears her iniquity', ['iniquity_borne'])
    if ask == 'she_is_clear':
        ink('30:16, 5:31', '"he shall bear HER iniquity" — "her iniquity" five Torah seats, the suspected wife\'s among them (computed at the reading)')
        move('CALLED cold_run_naso.sotah(husband_clean) -> %s / %s [IMPORT, live]' % (SOTAH_CLEAN[0], SOTAH_UNCLEAN[0][:30]), '5:31 "the man shall be clear of iniquity and that woman shall bear her iniquity" — the phrase\'s first seat, the roles reversed here')
        move('Nedarim 83a:1', 'she who transgressed relying on his annulment incurs no lashes')
        return out('she is clear — the iniquity his', ['iniquity_borne'])
    if ask == 'measure_of_good':
        move('Sifrei 156:2; Sanhedrin 100a:17-18; Yoma 76a:7', 'if one who causes his fellow to stumble takes his place under the measure of PUNISHMENT, which is small, how much more under the measure of GOOD, which is great')
        dat('the row measure_of_good_ratio = %s' % data['measure_of_good_ratio']['value'])
        return out('the a-fortiori from the two measures — the ratio a recorded parameter', ['accepted'])
    if ask == 'oath_to_harm_himself':
        move('CALLED cold_run_vayikra5.graded_offering(utterance_oath, option) -> %s [IMPORT, live]' % OATH_OPTION[0], 'the option template "to do evil or to do good" — an oath to harm HIMSELF binds (Shevuot 27a:6); to harm others not (27a:7)')
        return out('the affliction oath the oath to harm oneself — bound', ['vow_bound'])
    if ask == 'vows_and_oaths_one_class':
        ink('30:14', '"EVERY VOW and EVERY OATH of binding" — the two words one class for the husband\'s power')
        move('Nedarim 80b:3-4 (Rav Yehuda; Rav Ashi)', '"these are the vows AND OATHS he annuls" — or oaths inside "vows" ("like the vows of the wicked" — a nazirite, an offering, an oath)')
        return out('vows and oaths one class for the annulment', ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F7: THE STATUTES (Num 30:17 and the chapter whole) ====================================================
def the_statutes(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'likening_both_ways':
        ink('30:17', '"these are the statutes which the LORD commanded Moses, BETWEEN A MAN AND HIS WIFE, BETWEEN A FATHER AND HIS DAUGHTER" — %s, %s one seat each (computed)' % (BETWEEN_MAN, BETWEEN_FATHER))
        move('Sifrei 156:3; Nedarim 68a:1 (R. Yishmael\'s school)', 'the father likened to the husband and the husband to the father IN EVERY RULE STATED — the chapter\'s engine (four rows end on it); the betrothed\'s joint annulment from it')
        return out('the footer likens both ways — the engine of the chapter', ['accepted'])
    if ask == 'in_her_youth_her_fathers_house':
        ink('30:17', '"in her youth, her father\'s house" — "in her youth" %s (computed)' % IN_HER_YOUTH)
        move('Sifrei 156:3; Nedarim 70a:7', 'the father bounded to her youth in his house; the husband\'s power reaching past it; her father dead, she is still "in her father\'s house"')
        return out('the father\'s bound; the husband\'s reach', ['accepted'])
    if ask == 'fathers_gains':
        move('Ketubot 40b:4, 46b:6; Kiddushin 3b:7', 'the footer\'s clause for her gains and her betrothal money — a taught transfer')
        return out('the clause generalized — labeled', ['accepted'])
    if ask == 'the_receipt':
        ink('30:1', '"and Moses SAID to the children of Israel ACCORDING TO ALL that the LORD commanded Moses" — the formula\'s %d seats, this alone after a speech verb (computed); the register gate\'s finder read only "AS the LORD commanded" until this sitting' % len(RECEIPT2))
        move('THE REGISTER GATE (register_census.receipts, the second form)', 'the eleven seats of "according to ALL that the LORD commanded" joined the census; 30:1\'s class computed on the running world and declared from the print — the class of one (the 9b debt (v))')
        return out('the receipt that closes a speech — in the census by the finder\'s second form', ['accepted'])
    if ask == 'the_register_gate':
        ink('30:17', '"these are the statutes" — the footer (%s); its block (Lev 27:34, Num 30:17] holds the walk\'s daemons, law_vows the thirteenth' % FOOTER)
        return out('the footer DAEMONS — law_vows joined its block', ['accepted'])
    if ask == 'case_structure':
        ink('30:3-16', 'two "when" cases at %s and seven "and if" branches at %s; the chapter\'s other two "ki" are "because" (%s) — computed' % (WHEN, AND_IF, KI_SEATS[2:]))
        return out('two when, seven and-if — the draft\'s nine rows', ['accepted'])
    if ask == 'clock_words':
        ink('30:6-16', '"on the day of his hearing" %s; "from day to day" %s; "after his hearing" %s — computed' % (DAY_OF_HEARING, DAY_TO_DAY, AFTER_HEARING))
        return out('the clock the chapter\'s only number', ['accepted'])
    if ask == 'doubled_verbs':
        ink('30:3-16', 'five doubled verbs adjacent — %s; "annul, he annuls" %s, "be, she shall be" %s, "silent, he is silent" %s, "swear an oath" %s' % (DOUBLED, ANNUL_ANNUL, BE_BE, SILENT_SILENT, SWEAR_OATH))
        return out('five doubled verbs — every one read by the shelf as law', ['accepted'])
    if ask == 'the_line':
        ink('30:2-17', 'ONE line on the tape — Moses\' speech at the counter\'s day, no marker; the statutes commanded on israel')
        return out('the statutes of vows commanded — one write, no timer, no close', ['commanded'])
    if ask == 'installed_by':
        ink('30:2', 'no divine frame — the frame verbs %s both Moses\'' % FRAME_VERBS)
        move('THE LOOP step 3 (installation_parameters.yaml)', 'the installing acts erect institutions; Moses\' relay erects none and the chapter has no case (36:6\'s relay is a case-born output): BOOT with the class named — the second pass decides')
        return out('installed_by boot — a statute relayed in Moses\' voice, the class named', ['accepted'])
    if ask == 'all_generations':
        move('Bava Batra 120b:1 (Rav Ashi); Nedarim 78a:2', '"this is the thing" here and at Lev 17:2 — the vows\' law for all generations; the addressees Aaron, his sons and all Israel')
        return out('for all generations — the relay not case-bound', ['commanded'])
    if ask == 'placement_after_the_calendar':
        move('Nedarim 78a:9-11, 78b:2 (ben Azzai)', '"the festivals are stated, the vows\' portion not with them" — yet it stands NEXT to the festivals\' (28-29 then 30): the festivals need experts, the vows do not')
        return out('the chapter\'s placement read as law — next to the calendar, not of it', ['accepted'])
    if ask == 'two_kinds_of_ki':
        ink('30:3, 30:4, 30:6, 30:15', '"ki" as WHEN at the two case heads, as BECAUSE at 30:6 and 30:15 (computed: %s)' % KI_SEATS)
        return out('one particle, two jobs — the parse decides', ['accepted'])
    return out('no verdict in span', [FX.NONE])

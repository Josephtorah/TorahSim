# LAW ERA block 3 — full oral scan of Exod 21:28-36 (goring ox)

RESUME HEADER (keep current — updated every bite)
=================================================
- Span: Exod 21:28-36 (block 3 of TOP10_LAW_BLOCKS.md; blocks 1-3 subdivide
  frozen unit exo_21_the_ordinances, 21:1-37 — this is the LAST block inside
  Exod 21; NOTE verse 21:37 (ox/sheep theft opener, Hebrew numbering) sits
  outside blocks 1-3 as listed — flag for owner at block-4 census / chapter
  gate).
- Census 2026-08-11 (law03_census.py): 1,702 distinct listings anchored at
  21:28-36 → 1,174 READABLE + 6 TANAKH-VERSE = 1,180 required, 522 OUT
  (standing scope rulings), 0 UNRULED. 1,263 needed segments, He 861k ch.
- 50 of the 1,180 were ALREADY read in blocks 1-2 (dual-anchor listings;
  shared chapter ledger logic/oral_audit/ledgers/Exod_21.jsonl is the
  cursor), so block-3 remaining at start: 1,124 readable + 6 tanakh = 1,130.
- Seen-segs seeded from law02_seen_segs.txt (3,854 segs, blocks 1+2
  cumulative) — segs already read print as "[read earlier]", ledger rows
  still written. Same-ledger dedup, NOT scope narrowing: every required
  listing still gets its row.
- Kit: law03_census.py / law03_dump.py / law03_queue.json / law03_texts.sqlite
  / law03_seen_segs.txt (scratchpad; census+dump+notes mirrored to repo
  logic/law_era/scratch_mirror/). Bite = one default-cap (32k ch) dump call
  → law03_batchN.txt → read → digest below. Dump calls MUST redirect:
  python3 law03_dump.py > law03_batchN.txt
- Progress: bite 10 done (61 listings — CHIZKUNI whole + crossrefs,
  TUR code layer CM 389+410 + HaArokh, RABBEINU BAHYA whole, Kitzur
  Baal HaTurim, Bekhor Shor opening). Ledger 4,331 rows. Remaining:
  394 readable + 6 tanakh. Target: 4,731.

MARQUEE FINDS SO FAR (index — details in batch digests)
-------------------------------------------------------
- (B10) CHIZKUNI'S LAW-AND-ECONOMICS OF THE FLAT TARIFF (21:32):
  slaves habitually live AMONG THE CATTLE (feeding, guarding), so
  ox-kills-slave is FREQUENT and valuation suits would multiply
  ("this one says my slave was worth so-and-so, that one says less")
  → the Torah fixes 30; a free man's death by ox is RARE (מלתא דלא
  שכיחא) → individual assessment is affordable. Statutory pricing
  justified by case-frequency and litigation cost.
- (B10) BAHYA'S DEMONOLOGY OF THE GORING OX (21:28): the killer-ox
  carries the power of the PRIMORDIAL SERPENT; "in Nisan the SATAN
  DANCES BETWEEN ITS HORNS"; the ox draws from Judgment (Ezekiel's
  ox-face on the LEFT of the Chariot) — fused with the Taanit
  isomorphism: PLAGUE is 3 deaths in 3 days exactly as mu'ad is 3
  gorings in 3 days (epidemic threshold = forewarning threshold; one
  day apart is coincidence in both systems).
- (B10) BEKHOR SHOR'S HEIRS' OPTION (21:29-30): peshat of וגם בעליו
  יומת — an owner who RELEASED the ox to kill his enemy is a murderer
  ("like one who aims a jet of water"); otherwise the HEIRS CHOOSE:
  death or money. The cofer's אם exists because "most people find it
  shameful to take coin for a father's blood" (the donkey-case
  refusal: "since he's assessed like a slave — I don't want it, it
  demeans me"). Chizkuni concurs: the court sets cofer "since the
  heirs consent."
- (B10) JOSEPH'S 300 = 10 × 30 (Chizkuni + Bahya, Gen 45:22):
  Benjamin's three hundred silver = TEN TIMES the slave-price — the
  Gittin fine for selling a slave to gentiles (ten times his value)
  applied to the brothers' sale of Joseph, with OUR 30-shekel tariff
  as the unit. Kitzur Baal HaTurim's battery beside it: פדיון נפשו in
  gematria equals BOTH "the damager's value" and "the victim's value"
  (the valuation-machloket encoded in one word); Canaan's עבד עבדים
  יהיה = 30 (the tariff inside Noah's curse); ולא יאכל = ולא הנאה.
- (B9) RAMBAN ROOTS THE STONING IN THE FLOOD COVENANT (on Gen 9:5):
  "from the hand of every beast I will demand it" = every beast that
  kills a man dies, a King's decree — "and THIS is the meaning of
  סקול יסקל השור: not to fine the owner, for even a WILDERNESS ox is
  liable — commanded to the Noahides as to Israel." The ox executed
  under Genesis 9; the ownerless-ox inclusion explained at covenant
  level.
- (B9) THE GRAMMAR WAR OVER או: Rashi and Radak read או=אם across
  Tanakh from OUR או נודע (the B8 hub); Ramban (21:31): "they are all
  FALSE WITNESSES — understand each in its place" — או is additive. A
  frontal machloket over the block's grammar exports. Beside it, Ibn
  Ezra's morphology rows: ולא ישמרנו = ישמרנהו with the heh SWALLOWED
  into the nun (our verse as his nun-assimilation exhibit).
- (B9) THE STONED OX FILED AS A CHOK (Tanchuma Mishpatim 7): on the
  list of laws "the evil inclination and the nations object to" —
  with pig, shatnez, the scapegoat — "I the LORD decreed them; you
  have no license to question." Directly against the block's
  rationalizing thread (Chinukh's "intelligible matter," Ibn Ezra's
  victim-blame-blockers, TT's apologia): the corpus carries BOTH
  filings of the same statute.
- (B9) RADAK'S POLEMIC ROW (Ps 22:32): the christological "they
  pierced my hands and feet" is built by misreading כארי as OUR
  כי-יכרה dig-verb ("they drove nails") — Radak dismantles the
  proof-text; and at Ps 40:7 the same root gives אזנים כרית לי —
  "EARS you dug for me": obedience over sacrifice (no sacrifice
  clause in the Decalogue; the tamid instituted because of sin).
- (B8) THE GOLDEN-CALF RANSOM PRICED OFF OUR OX-TARIFF (Tanchuma Ki
  Tisa 6): Moses fears the atonement price — bids run a talent of
  silver, 100 (the defamer: "we defamed God — 'these are your
  gods'"), 50 (the rapist: "we raped the commandment"), and R. Yehudah
  bar Simon's THIRTY SHEKELS from אם עבד יגח השור: "they exchanged His
  Glory for the likeness of an OX — each owes the slave-tariff." God:
  none of these — HALF A SHEKEL. And איך אשיתך בבנים (Jeremiah) read
  as cofer-assessment language from יושת עליו: "I was your defense
  counsel; you made Me the prosecutor who SETS the liability."
- (B8) THE STONE-CLEARER PARABLE (Lekach Tov 21:29): a man clears
  stones from his field into the public road; the chasid: "why do you
  move them from what is NOT yours into what IS yours?" He laughs —
  then sells the field and trips on his own stones. The public domain
  is the only estate you keep. Same row: fines aren't judged in
  Babylonia, but SEIZURE stands and the yeshivot EXCOMMUNICATE whoever
  keeps a standing damager at home (R. Natan's no-bad-dog rule) — the
  post-semikhah enforcement regime.
- (B8) RASHI'S GRAMMAR HUB SITS IN OUR BLOCK: או=אם sourced from או
  נודע at FOUR sites (Isaiah 27, Leviticus 4 + 26, Numbers 5); אם=אשר
  from אם כופר at Job 42:8; the GIHON river named "goring" from כי
  יגח ("it goes goring and roaring"); Daniel's אתכרית from כי יכרה;
  והועד בבעליו on the plural-of-lordship list (Gen 20:13). And the
  slave-shekel converted to "half an ounce by the honest weight of
  COLOGNE" — the tariff localized to the Rhineland.
- (B8) NOAH'S ARK AS COFER (Midrash Aggadah Gen 6:14): the ark's pitch
  (כפר) joined by gezerah shavah to אם כופר יושת עליו — "they had
  incurred death by Heaven, and the ark ATONED for them": the ransom-
  clause read back into the flood.
- (B7) TARGUM JONATHAN INLINES THE ORAL LAW into the verse text:
  "testified before his owner's face THREE TIMES" (21:29); the owner
  dies "by a death SENT UPON HIM FROM HEAVEN"; the cofer is "a
  MONEY-FINE set by the SANHEDRIN OF ISRAEL" (21:30); the slave
  written as "CANAANITE" (21:32); the pit dug "IN THE MARKET" (21:33,
  public-domain bor inlined); the victim keeps the carcass "AND THE
  HIDE" (21:36). Six rulings compiled into Aramaic scripture — the
  halakhic-compiler pattern from block 2 again. Onkelos meanwhile
  renders bein/bat as "son/daughter OF ISRAEL" (the gentile-victim
  exemption in translation) and אם כופר as "if MONEY" (Minei Targuma's
  essay defends it against cofer-as-atonement).
- (B7) PARSER AMBIGUITY IN THE ROOT-PRINCIPLES (Rambam, Shorashim
  8:5): Hebrew לא is one word for negation AND prohibition, and OUR
  ולא יכסנו is the paradigm case — R. Elazar's "need not divide" for
  the bird-offering is tested against "need not cover"?! — refuted
  because בעל הבור ישלם proves covering is required. The
  consequence-clause disambiguates the operator, stated as method in
  the mitzvah-count's foundations.
- (B7) THE DEATH-TARIFF PRICES THE FREEDOM-GRANT (MT Slaves 3:14): the
  severance grant (ha'anakah) to the freed Hebrew slave has a floor of
  30 sela — "like the thirty of the slave's fine, of which it says
  יתן לאדוניו." The goring-ox's Canaanite-slave death-tariff recycled
  as the Hebrew slave's exit-gift floor (block-1 severance-table
  crossover).
- (B7) THE COERCION-EXEMPTION PROMOTED TO THE ALTAR (MT Altar-
  Forbidden 4:3): a stadium ox that killed is KOSHER FOR SACRIFICE —
  "for it is as one coerced." And SMaG's ethics coda: Rav Yehudah —
  "who wants to be a CHASID should keep the laws of NEZIKIN" (the
  first pious ones buried their thorns three tefachim so the plow
  wouldn't raise them).
- (B6) "THE STONED OX IS ENTIRELY MONEY — its stoning is a decree of
  Scripture" (R. Yosi b"r Bun, Yerushalmi Sanh 1:1, answering whether
  the money-side could be judged by 3 while the stoning needs 23). And
  the DOUBLE ANSWER of R. Yochanan b. Zakkai to AGNATOS THE GENERAL on
  וגם בעליו יומת: to the Roman — "a bandit's accomplice is as the
  bandit"; to his students — the 23-court isomorphism with
  interrogation. Exoteric reed-answer, esoteric law.
- (B6) THE STONED ROOSTER OF JERUSALEM (Niddah 8a): a rooster was
  stoned in Jerusalem for killing a person — the ox-protocol actually
  executed on a chicken (all species via shor-shor from Shabbat).
  R. Yirmiyah's twin puzzle (Yerushalmi Pesachim 2:1): a FIRSTBORN
  DONKEY that kills — neck-breaking (its own law) or stoning (the
  killer's law)? Two death-protocols collide on one animal.
- (B6) INSANITY DEFINED BY THE MU'AD TEMPLATE (Chagigah 4a): "who is a
  shoteh? one who loses everything given him" — argued from the ox
  "gored an ox, a donkey, a camel — mu'ad for ALL": the forewarning
  state machine borrowed to classify human minds.
- (B6) THE HALF-SLAVE SPLIT ACROSS THE STATUTE (Gittin 42a): killed by
  an ox, he draws half KENAS (15 shekels to his master) + half COFER
  (to his heirs) — one person, both tracks. Rambam completes the
  pattern (MT Damages 10:14, his own נראה לי): a tam killing a slave
  unintentionally pays half the slave's VALUE from its body — "as if
  it killed his ox or donkey."
- (B5) SHIMON HaAMSONI'S RETREAT lives in OUR verse (BK 41b, on את
  בשרו): the tanna who expounded EVERY את in the Torah withdrew at
  "fear את the LORD" — "as I received reward for the expounding, so I
  receive reward for the withdrawal" — until R. Akiva: "include Torah
  scholars." The quantifier-integrity crisis of the whole drash-system,
  anchored on the stoned ox's flesh-ban.
- (B5) DOCUMENT DUE-PROCESS FROM THE OX (BK 112b): R. Yochanan — a
  note may not be authenticated outside the party's presence, from
  והועד בבעליו: "let the owner of the ox come and stand over his ox."
  The B1 testimony rule extended to civil paperwork.
- (B5) THE FINE RIDES ON THE STONING (Resh Lakish + Rabbah, BK 43a):
  unintentional killing → no stoning → NO 30-shekel slave-fine and NO
  cofer — "while the ox is under stoning the owner pays; no stoning,
  no payment." Money-liability coupled to the animal's capital status
  (against R. Yochanan's אם-ribbui, Abaye pressing the symmetry).
- (B5) THE PIT IS MEASURED BY ITS VICTIM (Yerushalmi BK 1:2): R.
  Elazar HaKappar — a pit is "the fill of the faller: even a chicken,
  even a camel"; same sugya: שמירת נזקין כשמירת קניין — guarding-duty
  tracks acquisition-modes. And the escalation counter can run on
  PURSUITS (4:2): three chases with assessed goring-intent make a
  mu'ad — no completed goring needed (Rav: killed 3 gentiles → mu'ad
  for Israelites).
- (B4) THE SADDUCEE TAUNT ANSWERED BY INCENTIVE DESIGN (Mishnah
  Yadayim 4:7): "my ox, no mitzvot — I'm liable; my slave, who has
  mitzvot — exempt?!" The Pharisees: the ox has no daat, the slave
  does — "if I provoke him, he will go burn another's grain-stack and
  make ME liable." Moral hazard argued inside the Mishnah; joins the
  block-2 Sadducee-filter thread.
- (B4) TWO PHILOSOPHIES OF HALF-DAMAGE (Ketubot 41a): Rav Papa — it's
  MONEY: oxen are presumed wild, he owes it all, the Torah PITIED the
  not-yet-warned owner; Rav Huna b. R. Yehoshua — it's a FINE: oxen
  are presumed guarded, he owes nothing, the Torah FINED him so he'd
  guard. The tam's half-payment as mercy-discount vs deterrence-fine.
- (B4) THE PROHIBITION TRACKS THE VERDICT, NOT THE EXECUTION (Mishnah
  Keritot 6:2): stoning carried out and the case then dissolved →
  carcass PERMITTED in benefit; case dissolved before stoning → the ox
  returns to graze in the herd. The issur hangs on a standing verdict,
  not on the stones.
- (B4) MU'AD FOR SABBATHS ONLY (Tosefta BK 4:5): the forewarned-state
  is CONTEXT-INDEXED — gores on Sabbaths, tame on weekdays; reverts
  after three goring-free Sabbaths. And Tosefta 4:6 carries R.
  Yehudah's anti-tradition: wilderness/Temple/dead-convert's ox EXEMPT
  from stoning ("these have no owner") — the direct opposite of the
  seven-shor inclusion (B1/B3).
- (B3) KING YANNAI SUMMONED BY OUR VERSE (Ikar Tosafot Yom Tov, Sanh
  2:2): his slave killed a man; Shimon b. Shetach summons the king to
  stand before the Sanhedrin because והועד בבעליו ("warning was given
  to its OWNER") — "a slave is as his owner's property," so the
  ox-arraignment clause reaches the throne. Yannai sits, the judges
  cower, Shimon's curse kills them — and "a king neither judges nor is
  judged" is born from the failure. Royal accountability, sourced in
  the goring-ox docket.
- (B3) Mekhilta DeRabbi Shimon's forfeiture doctrine: רעהו ("his
  fellow") excludes the gentile AND the resident alien — but שלם ישלם
  makes them pay FULL damage even for a tam, and the prooftext is
  הופיע מהר פארן ("He shone forth from Paran... toward all the
  nations"): the refused Sinai-offer grounds the asymmetry — an older
  twin of R. Abbahu's Habakkuk forfeiture (B2).
- (B3) Hon Ashir's NUMERIC MACHINE: בור ("pit") in reduced gematria =
  10 (2+6+2) — the lethal 10-handbreadth depth encoded in the word
  itself, with a kabbalistic warrant for WHEN reduced-counting is
  licit (death/mourning contexts). Twin of the Gra's vav-machine (B2).
- (B3) MdRShbY: את איש — the ox must intend THIS victim ("until it
  intends him"); and the carcass-halving verse is valid ONLY between
  equal-value oxen ("the Torah spoke only when the two are equal") —
  else the tam would pay more than the harm, or the damager would
  profit; both barred (בעליו שלם ישלם — owners pay, never take).
- (B2) The GRA's ORTHOGRAPHIC MACHINE on the pit: three spellings — כי
  יפתח איש בור FULL vav, או כי יכרה איש בר DEFECTIVE, בעל הבור ישלם
  FULL — read as: one dug a full pit (10 handbreadths), one dug a
  defective one (9), another added the 10th; who pays? "the owner of
  the FULL pit" — the COMPLETER. The 9+1 finisher-liability rule
  encoded in plene/defective spelling (Shenot Eliyahu likkutim; TT adds
  his simpler injury-tier/death-tier mapping).
- (B2) Torah Temimah's goring-ox APOLOGIA at רעהו ("his fellow"): the
  Israel/gentile asymmetry answered by the Talmud ITSELF on the same
  page — R. Abbahu's ראה ויתר גוים ("He saw and released the nations",
  Habakkuk 3:6): the seven Noahide laws unkept FORFEIT property-
  protection; the rule targets lawless peoples "like predatory beasts,"
  and any nation keeping them — "most nations of this time" — has "law
  with us as Israel's law" (restated at the 23:5 donkey-loading row).
  TT then reads the Mishnah's odd wording (opens "Israel," closes
  "commoner") as precisely encoding the Temple/gentile liability
  lattice — killing the Bach's emendation. Same historicization thread
  as block-2's Netinah LaGer Sadducee-filter.
- (B2) The tam makes victim and damager PARTNERS in the living ox (R.
  Akiva, halakha — victim's consecration of it takes effect), and חס
  רחמנא עליה דמזיק ("the Merciful One pitied the damager"): the damager
  SHARES the carcass's post-mortem appreciation (R. Yehudah) — capped
  by שלם ישלם: "owners PAY, owners don't COLLECT" (no profiting).
- (B2) The ox gets the court but NOT the mercies: R. Abbahu — all TEN
  capital-vs-money protections absent for the stoned ox except the 23
  judges; לא תטה משפט אביונך ("do not tilt your poor man's case") read
  as: a man needs a 2-vote majority to convict, the OX can be convicted
  by ONE.
- (B1) HYSTERESIS in the forewarned-state machine: escalation tam→מועד
  ("forewarned") needs 3 goring DAYS (R. Yehudah), but reversion needs
  only ONE day of children petting it un-gored (R. Meir) — Torah Temimah
  grounds the asymmetry in habit-psychology (acquiring slow, breaking
  hard, so one abstention proves reversion) and EXPORTS it to rescue
  Maharam of Rothenburg's 90-repetitions משיב הרוח ("who makes the wind
  blow") rule against all his attackers: cessation-of-habit follows the
  one-day standard. State-machine thresholds → liturgical habit law.
- (B1) The ox gets FULL capital due process — כמיתת בעלים כך מיתת השור
  ("as the owner's death, so the ox's death"): 23 judges, verdict only
  in the ox's PRESENCE, warning, cross-examination, terefah-ox exempt.
  And והועד בבעליו ("warning was given to its owner") is the SOURCE of
  no-testimony-absent-the-party: "let the owner of the ox come and
  stand over his ox." Rashi's cut: only acquittal-mercies don't extend
  ("we need not seek merit for the ox").
- (B1) R. Yishmael at אם כופר ("if a ransom"): "come and see the mercies
  of the Holy One — a man PURCHASES HIMSELF from Heaven's hand with
  money"; the אם is obligation. Cofer = atonement that is ALSO a
  collectible debt: two partners each pay a FULL cofer (each soul needs
  its own atonement), yet the court seizes it like any debt because it
  belongs to the victim's estate.
- (B1) שור שור שבעה — 'ox' 7x → woman's, orphans', guardian's, Temple's,
  WILDERNESS/OWNERLESS ox, dead convert's ox all stoned: guilt attaches
  to the ANIMAL, independent of any owner.

BITE DIGESTS
============
## Bite 1 (batch 1) — 48 listings: TORAH TEMIMAH 21:28-33
- 21:28: goring = HORN only; TT explains why the Zedekiah iron-horns
  proof (Kings) precedes the Torah proof — purpose-built horns prove
  exclusivity. יגח for man vs יגוף (v.35) for beast: man has מזלא
  ("mazal/fortune") — TT proves Rashi's Shabbat-53b angel-reading over
  his local self-guarding reading, from "forewarned-for-gentile is not
  forewarned-for-Israelite". Stadium-trained ox exempt (כי יגח — "when
  it gores", not when they MAKE it gore); TT defends Raavad against
  Migdal Oz's misreading. All death-modes = goring. Every beast = 'ox'
  (gezerah shavah to Decalogue-2); TT emends the Mishnah's list from
  Tosefta BK 6:7. Minor victims count. ולא יאכל: slaughter after
  verdict still forbidden; benefit forbidden; forbids in any admixture;
  skin/blood/fat in via את; but DUNG permitted (mere excretion — and
  tam pays from its body, not its dung). בעל השור נקי: clear even in
  Heaven's court (R. Yehudah).
- 21:29: the FIVE-WAY tam/mu'ad fork as a block (witnesses; cofer; 30
  for slave; full vs half damage; estate vs body) + TT on the omitted
  sixth (tam exempt by confession — half-damage is a FINE) and why the
  Mekhilta lists only what THIS passage innovates. Hysteresis + Maharam
  Rothenburg export (MARQUEE above). One-owner continuity: gored then
  consecrated/ownerless → exempt (death, arraignment, verdict under ONE
  owner; TT emends Rambam's text to say so). Due-process battery
  (MARQUEE above). ולא ישמרנו: tied+locked yet escaped — mu'ad layer
  exempt, tam layer still pays (reduced guarding suffices for mu'ad);
  the four bailees step "under the owner". Woman=man for all Torah
  deaths; her cofer to HER heirs not the husband (cofer pays only after
  death → expectancy, and husbands don't inherit expectancies).
- 21:30: FULL cofer not half (partners); payable only AFTER victim
  dies; unintentional cofer like intentional (אם-rebus); R. Yishmael's
  mercy (MARQUEE above); פדיון נפשו = VICTIM's value not payer's; עליו
  ולא על האדם — a human killer pays no cofer (Rashi: the case is
  deliberate-without-warning). TT harmonizes Rashi "cofer is money"
  with Rambam "cofer is atonement": Rashi only excluded FINE-status
  (hence payable on own confession).
- 21:31: minors, tumtum/androgynos, his OWN children (though he
  inherits the cofer), converts (no heirs → no cofer → still stoned —
  קמ"ל each). כמשפט הזה: ox-vs-man pays like ox-vs-ox (tam half, mu'ad
  full); הזה exempts the ox from the FOUR human-tort payments — an ox
  damaging a man stays in the property-damage class (Rambam's
  rationale).
- 21:32: slave tariff — unintentional like intentional; CANAANITE slave
  (TT's own proof, sharper than Mizrachi's: a Hebrew slave's fine
  would go to his HEIRS, this one goes לאדוניו "to his master"); flat
  statutory 30: worth 100 maneh → 30, worth a dinar → 30; Tyrian
  coinage peg; slave-awaiting-manumission-writ gets NO fine (no
  master); wife's melog-slave: fine to HER (usufruct isn't ownership).
- 21:33: pit law opens — why stated despite k"v from ox (pit's whole
  making is for damage vs ox moves-to-damage); bor/shiach/cave all in,
  10 tefachim = death-threshold (9 = injury); TT defends Rashi's
  "standard pit = 10" vs Joseph/Jeremiah deep-pit counterexamples
  (utility pit vs prison pit); opener AND digger liable even in public
  domain; digger-after-digger: the 9+1 finisher is liable.
- Ledger: 3,601 → 3,649. Remaining: 1,076 readable + 6 tanakh.

## Bite 2 (batch 2) — 43 listings: TORAH TEMIMAH COMPLETE (21:33-36 + dual-anchor 22:4, 22:10, 23:5, 23:6)
- 21:33 (pit, continued): אין עונשין מן הדין ("no punishment by
  inference") — digging written separately because pit-liability is
  itself a novum (public-domain pit "made his though not his") and a
  novum stays confined to its text (TT reconciles Mekhilta with the
  Bavli's money-by-inference). Digging WITH RIGHT exempt (foundation
  trench, לאושין; TT sides with Sema: criterion is legitimacy of act,
  not location). Death needs 10 handbreadths; injury has NO minimum
  (Rambam from Tosefta). איש ולא שור — an ox that digs is no pit-owner
  (but the courtyard owner is, via his duty to fill). 9+1: the
  finisher liable for EVERYTHING (he moved the pit from injury-class
  to death-class). Bought/inherited/gifted pit liable — Yerushalmi
  derives from יכרה = acquire (like כריתי, Gen 50); Rambam prefers the
  Mekhilta's בעל הבור route. Covered properly + it rotted from within
  → exempt; standard: a laden wagon crosses it; "the Torah MINIMIZED
  the pit's guarding" (cover, not earth-fill — יכסנו vs יסתמנו).
  Handed to a guard → guard liable (TT finds the Mekhilta source
  everyone including the Gra's editor missed). The plasterer who
  narrows a too-wide pit CREATES the lethal airspace → liable via the
  covering-clause. Shmuel: liability for its AIR, all the more its
  IMPACT; a 10-high MOUND in public domain liable (TT harmonizes
  Rashi/Tur vs Rambam: self-formed mound = mere gramma unless 10).
  "Manner of falling": startled forward by the digger's voice → pit-
  owner liable; backward → exempt; the frightener himself always
  exempt (gramma-of-gramma). שור ולא אדם: a MAN dying in the pit →
  owner EXEMPT — TT's contributory-negligence rationale: a lethal
  fall needs total inattention, so the victim caused it (unifies
  Rambam's death/injury split and the day/night rules). חמור ולא
  כלים; "for vessels, breaking IS their death." All species in via
  כסף ישיב לבעליו ("whatever has an owner"); shor/chamor = the common
  case.
- 21:34: owner however he owns (self-dug, beast-dug, bought,
  inherited). Payment in ANYTHING worth money, even BRAN — with
  movables everything is מיטב ("best": unsold here, sells in another
  town); the dual-anchor 22:4 row explains why מיטב waits for the
  field-damage law (first payment context requiring LAND). והמת יהיה
  לו battery: pit-owner must HAUL THE CARCASS UP; disqualified-
  consecrated ox → exempt ("whose the carcass is" — he may not benefit
  from it); excludes LAND damage (undermined public ground) and MAN
  ("no benefit from his corpse"); carcass to the VICTIM at valuation,
  offset against damages.
- 21:35: opens נגיפה closes נגיחה — "this IS that" (root נגף names the
  blow, not the instrument; the close fixes horn). Minor's ox exempt —
  but the court APPOINTS A GUARDIAN for a habitual gorer. רעהו
  excludes Temple-property and the idolater — TT's apologia (MARQUEE
  above). ומכרו addressed to victim+damager, not the court: PARTNERS
  (MARQUEE above); slaughtered → still sold, מכל מקום. וחצו את כספו
  ("THIS one's money") → tooth-and-foot in public domain exempt even
  from half (beast has right-of-way; don't leave produce in the
  street); יחצון (extra) → horn pays half EVEN in public domain
  (blocks the zeroing k"v). R. Meir vs R. Yehudah on וגם את המת
  יחצון: half the death-depreciation vs damager-shares-appreciation
  (nafka-mina: carcass 100 at death, 120 at trial).
- 21:36: שלם ישלם — owners pay, never collect (mercy capped). Money ↔
  beast equivalence (gezerah shavah of the two והמת יהיה לו). Rav
  Kahana→Rava: the carcass-to-victim clause exists for DEPRECIATION —
  from the moment of death the carcass stands in the VICTIM's domain
  (later rot is his loss); and it is a RELIEF for the damager (his
  option), not a duty.
- Dual-anchor rows: 22:10:6 — the bailee's oath "between the two"
  excludes a married woman (owns nothing to pay with); TT leans to
  obligating her anyway (oath as claimant-appeasement + woman=man for
  this parashah). 23:5:2 — שונאך read "he who hates YOU" (TT's
  father-in-law the Ramah): resolves licensed-hatred vs
  love-your-neighbor; gentile-donkey historicization restated. 23:6:1
  — ox gets the court, not the mercies (MARQUEE above).
- Ledger: 3,649 → 3,692. Remaining: 1,033 readable + 6 tanakh.

## Bite 3 (batch 3) — 71 listings: MEKHILTA DeRABBI SHIMON whole + MEKHILTA DeR. YISHMAEL rows + SIFREI + MISHNAH SPINE + BARTENURA + HON ASHIR + IKAR TYT
- MdRShbY 21:28-30: stadium ox = "coerced" (מעושה); all species via כי
  יגח מכל מקום; victim-specific intent (MARQUEE above); offspring and
  HYBRIDS of the convicted stoned too; sinews/bones/horns forbidden
  like flesh; "not even to dogs" = benefit ban. THREE tannaitic
  readings of בעל השור נקי ("the owner is clear"): Ben Azzai — clear
  of the WHOLE value; R. Elazar b. Azariah — clear of fetus-payments;
  R. Eliezer — clear of half-damage. הוא = CERTAIN gorer, not
  doubtful. Warning before court AND owner (pairing v.29 with v.36's
  או נודע). The extra בעליו excludes the borrower who borrowed it as
  tam and it emerged mu'ad. No-intelligence owners (deaf/insane/minor)
  exempt from cofer. Husband doesn't inherit her cofer ("he does not
  inherit his wife in the grave"). Ownerless ox STILL stoned (השור
  יסקל מכל מקום). Cofer is OBLIGATION (ת"ל ונתן); amount set by COURT
  not his own word; R. Yishmael b. R. Yochanan b. Beroka: redemption
  of the DAMAGER's soul → partners each owe a full atonement. NOTE the
  school-flip: Mekhilta d'R. Yishmael Nezikin 10:29 has R. Yishmael
  reading פדיון נפשו of the SLAIN (victim-valuation) — the two
  Mekhiltas carry opposite valuation traditions.
- MdRShbY 21:31-33: יגח יגח two gorings → tam+mu'ad, death+LIMB
  damages; five species מועד FROM BIRTH (wolf, lion, bear, leopard,
  bardelas). Canaanite slave-pair proof: "their law is one" (Hebrew
  slave/maid laws differ from each other). 30 = sanctuary shekel;
  payment IN COURT like the stoning. Slave-goring needs mu'ad + death
  (gezerah shavah השור יסקל). Pit: women liable; איש פרט לקטן AND פרט
  לגבוה — the Temple's pit exempt; liability only public-domain or
  opening-to-public (from ובער בשדה אחר); handed to the PUBLIC →
  exempt ("no owners"); partners' pit (איש איש); startled-backward
  exempt; man KILLED exempt but man INJURED liable (כסף ישיב לרבות
  הנזקים); species via Shabbat's שורך וחמורך; pit exempt for CHILDREN
  and SLAVES (שור ולא בן, חמור ולא עבד — against the k"v from the pit
  being "מועד לעולם").
- MdRShbY 21:34-36: every obstacle = bor-derivative (תולדות); carcass
  DELIVERY duty ("troubles himself until he brings it to him");
  disqualified-consecrated "has no owners." Five-mode battery
  (gore/bite/crouch/kick/push); Abba Chanin: BITING derived from ולא
  ישמרנו as "an additional guarding the verse added." Gentile/ger-
  toshav forfeiture + Paran (MARQUEE above). Tam pays only from its
  body: "here is the damager before you" (worthless ox = full
  discharge). Equal-value limitation (MARQUEE above). 3 DAYS not 3
  times; deaf/insane/minor owners: court appoints guardians, witnesses
  testify before the guardian, they pay. שור תחת השור = VALUE in money
  (can't dump a 5-sela ox on a maneh debt).
- Mekhilta d'R. Yishmael rows: R. Yoshiyah's recurring איש-או-אשה drash
  (women equalized in ALL damages — because the pit-verse says איש)
  vs R. Yonatan "unnecessary, בעל הבור ישלם covers it" — anchored 4x
  across Nezikin 6-9. R. Yitzchak's k"v: where death was imposed only
  money was taken → all the more money-only where no death. The
  parashah exists to EXTRACT the ox from the general rule to burden it
  (stoning). Owner preemptively slaughtered after verdict → forbidden.
  Rabban Gamliel: נקי = clear of the slave-fine (tam). The FIVE
  differences stated verbatim TWICE (Nezikin 10:18 at v.29, 12:7 at
  v.36). Moserah-case school-flip vs the Mishnah: Mekhilta's R. Meir
  says tam exempt / mu'ad liable, Mishnah BK 4:9's R. Meir says both
  liable (R. Eliezer there: "its only guard is the knife").
- Sifrei Bamidbar 160-161 (refuge-complex): no ransom for HUMAN
  killers — stated as a rebuttal of extending OUR cofer ("as ransom is
  given to Heaven's condemned, so to man's? ת"ל ולא תקחו כופר");
  condemned man who injures → liable; injured → others exempt on his
  body, liable on his property; post-verdict killer of him exempt.
- Mishnah spine + Bartenura: the FOUR AVOT architecture (why each of
  shor/bor/mav'eh/esh must be written — each lacks a property; the
  common denominator + מיטב); five tams/five mu'ads; born-forewarned
  list + snake always mu'ad (R. Eliezer: tame ones aren't); hekdesh
  exempt both ways; guardian-appointment for cheresh/shoteh/katan oxen
  + the reversion dispute (R. Meir: matured owner → ox back to tam; R.
  Yosi: stays in presumption); wall-scratching ox (intent isomorphism
  + אם-rebus cofer); consecration of a condemned ox void; Arakhin 3:1
  + 3:3 kula/chumra frame — slave flat 30, free man = his VALUE (the
  Mishnah's dmei-nizak in statutory form); AZ 5:9: the stoned ox on
  the forbidden-in-any-admixture list beside yein nesekh and eglah
  arufah. Mu'ad pays from the estate "even if the gorer isn't worth
  the damage" (Bartenura on מן העליה).
- Hon Ashir BK 5:5: the bor-gematria machine (MARQUEE above).
- Ikar TYT Sanh 2:2: the Yannai summons (MARQUEE above).
- Ledger: 3,692 → 3,763. Remaining: 962 readable + 6 tanakh.

## Bite 4 (batch 4) — 109 listings: MISHNAH TAIL + TOSEFTA BK (both recensions) + TOSAFOT YOM TOV + YERUSHALMI ROWS + BAVLI BK SPINE 2a-41a
- Mishnah BK 5:6-5:7: partners' pit — the SECOND user who left it open
  is liable (duty transfers by use); blind/impaired/night-walking ox
  in the pit → liable (a sound ox by day is on its own guard);
  children and slaves → pit exempt. The all-beasts master list: pit,
  the SINAI BOUNDARY, double-payment, lost-property, unloading,
  muzzling, kilayim, Shabbat — "Scripture spoke of the common case."
- Tariffs and lists: Bekhorot 8:7 — the flat-tariff table (5 firstborn
  / 30 slave / 50 rape-seduction / 100 defamer, all sanctuary-shekel
  in Tyrian maneh); Ketubot 40a defends flatness: "a pearl-piercing
  slave 30, any slave 30" — statutory fines ignore market value.
  Temurah 7:4: stoned ox on the BURIED list; AZ 5:9 + Zevachim 8:1:
  forbidden in any admixture — mixed 1-in-10,000 into offerings, ALL
  die. Chullin 5:3: R. Shimon exempts its slaughterer (slaughter of a
  benefit-forbidden beast is no slaughter), sages hold liable.
  Kiddushin 2:9/56b: betrothal with its flesh void, with its
  SALE-PROCEEDS valid; Ben Zoma sources the benefit-ban in נקי
  ("exits his property clean"); 56b leaves hanging where the
  half-cofer/fetus-money tannaim get the hide-ban.
- Keritot 6:2: verdict-tracking (MARQUEE above); contrast eglah arufah
  — beheaded → buried, "it came on doubt, its doubt atoned and left."
- Yadayim 4:7 + Rambam ad loc: the Sadducee taunt (MARQUEE above);
  Rambam: women/slaves/minors "their striking is bad" — judgment-proof
  but liable when freed.
- Sanhedrin 1:1/1:4 + Tosefta Sanh 3:1: ox in 23; the born-forewarned
  beasts — R. Eliezer: "whoever kills them first merits"; R. Akiva:
  23. Tosefta lists the STRIPPED mercies: ox-trials may open by day
  close by night, same-day conviction, majority of ONE convicts, all
  may argue either way, a merit-arguer may flip — the B1/B3 principle
  in tannaitic list form.
- Tosefta BK: 3:1 — split-state ox (mu'ad by horn, tam by tooth); no
  estate → mu'ad "goes out and seeks the estate." 3:2 — the
  assessment rule: never "take the carcass and give me a cow";
  before/after valuation, carcass stays with the victim. R. Akiva:
  tam goring a MAN pays FULL in the excess but from its BODY (יעשה לו
  — Bavli 5a: "R. Akiva broke his own sword"). 4:6 — the four-quadrant
  matrix: cofer+death (mu'ad killed); death-no-cofer (tam;
  impaired-owner's ox; victim a CONVERT or freed slave — no heirs);
  cofer-no-death (wall-scratcher; intended-beast/gentile/stillborn
  killed viable Israelite; R. Shimon exempts damages too — עד שיתכוון
  ליגח); neither (Samaritan victim, 8-month child). R. Yehudah's
  ownerless-exempt anti-tradition (MARQUEE above) + owner-continuity
  from killing through court-standing; valuation dispute AGAIN (R.
  Yehudah: assess the victim; R. Yochanan b. Beroka: assess the
  OWNERS). 5:4/5:7 — bought-as-tam-found-mu'ad = MEKACH TAUT (the
  tam-warranty voids the sale); the moserah four-way: Tosefta+Mekhilta
  R. Meir tam-exempt/mu'ad-liable vs MISHNAH's R. Meir both-liable;
  R. Eliezer b. Yaakov both exempt; R. Eliezer: "the ox's only guard
  is the knife." 4:5 — Shabbat-indexed mu'ad (MARQUEE above). 6:4/6:14
  — pit-victim rules + the PUBLIC-PIT PRESUMPTION TABLE: mid-road pit
  presumed of the BABYLONIAN PILGRIMS, plaza/karmelit of the town,
  mid-field of the field-owner; rivers and springs of ALL; Tosefta's
  own vessel-exclusion route (via ona'ah); tilted flask → liable.
- Tosafot Yom Tov: Arakhin 1:3 — ransom-for-Heaven's-condemned barred
  for man's-condemned from כל חרם לא יפדה (Lev 27 route, beside Num
  35's). BK 1:2 — hefker-ox damages: "who would claim it?"; TYT's own
  move: one-owner continuity imported from death-law to DAMAGES by
  אם-אינו-ענין off the seven-shor superfluity ("and this needs
  study"). BK 3:3 — Yerushalmi: בעל הבור ישלם = "owner of the DAMAGE"
  (no ownership-intent needed) vs tithing's "your grain." BK 4:5 —
  cofer only for viable children; doubt → owner keeps the money, but
  "to satisfy Heaven" pay even on doubt (cofer is atonement). Sanh
  2:2 — the full Yannai story + why kings of David's house still
  judge (דינו לבקר משפט; the decree spared them "so as not to
  contradict the verse").
- Yerushalmi rows: Ketubot 2:1 — PROBABILITY IN MONEY-LAW: gored cow,
  fetus beside it — "do most cows miscarry?" → attribute to the
  goring; R. Abbahu: in money we do NOT follow the majority — except
  R. Acha's rutting-camel case (one dead camel, the rutter did it).
  Ketubot 10:4 — the SEQUENTIAL-GORING WATERFALL (last victim a
  maneh, prior 50, first two a gold dinar) used as the model for
  investor profit-splitting ("oxen are like fixed shares"). Ketubot
  13:9 — NETTING: mutual debt offset derived from the two tams goring
  each other paying "in the excess." Kiddushin 1:4 — חיים שנים ישלם:
  the thief restores LIVE animals.
- Bavli BK spine 2a-41a (source-rows): horn from Zedekiah; nagifa=
  negiha; 10/9 tefachim; ox-vs-man (cofer vs four-payments); the
  tachat/netina/yeshalem/kesef gezerah-shavah battery; hekdesh
  problem + R. Shimon b. Menasya route; ישיב-even-bran vs
  land-only-court-seizure (victim who grabbed movables keeps them);
  the shor-vs-bor CHUMRA TABLE (9b); one-owner continuity + gmar-din
  (13b); woman=man; chicken-scratched pit — "איש בור ולא שור בור";
  fire-vs-ox ("had his OX killed a slave — 30"); R. Yehudah's
  four-goring count (תמל 1, מ 2, שלשם 3, ולא ישמרנו the 4th); R.
  Akiva "like the lower not the upper" + R. Yishmael court-addressed
  vs R. Akiva parties-addressed (33a); dmei-nizak vs dmei-mazik
  (27a, 40a); Ketubot 41a mamona/kenasa (MARQUEE above); Ketubot 42b
  + Rashba: יתן vs ונתן — when the 30-shekel vests (kenas timing);
  Ketubot 33b: stole a stoned ox and slaughtered — R. Meir fines 4/5
  even on a worthless beast.
- Ledger: 3,763 → 3,872. Remaining: 853 readable + 6 tanakh.

## Bite 5 (batch 5) — 93 listings: BAVLI BK TAIL 41b-112b + YERUSHALMI BK WHOLE + RASHI/TOSAFOT ROWS + BEN YEHOYADA + YAD RAMAH
- Bavli 41b-46a: the HaAmsoni story (MARQUEE above). Why נקי is
  needed: one might collect the slave-30 from a TAM's estate (slave-law
  is stricter — a sela-worth slave still fetches 30) — kra clears him.
  Resh Lakish/Rabbah couple fine and cofer to the stoning (MARQUEE
  above); Rav Dimi's אם-ribbui (unintentional cofer) vs Abaye pressing
  אם עבד symmetry. R. Shimon: victim-specific intent from the
  isomorphism. The seven-shor braita WITH R. Yehudah's ownerless-
  exempt dissent inline (44b — the Bavli home of the Tosefta
  anti-tradition). R. Eliezer's "only guard is the knife" — Rabbah:
  ולא ישמרנו = "it has no guarding anymore" (the mu'ad is beyond
  guarding); Abaye: then ולא יכסנו would mean pits can't be covered!
- Bavli 48a-55b (pit): yard-owner with duty-to-fill = digger (כי יכרה
  איש ולא שור, yet liability re-enters via the duty). R. Yishmael vs
  R. Akiva on which pit is "THE pit of the Torah" (public-domain vs
  owned-ground — both liable either way; R. Akiva: "the pit Scripture
  OPENED payments with"). Rav vs Shmuel: ונפל = manner-of-falling
  (impact) vs any-falling (air); mound-liability rides on Shmuel's
  reading. 9+1: the finisher "did the death" (והמת יהיה לו). R.
  YEHUDAH INCLUDES VESSELS in pit-liability (או לרבות — 53b) vs
  rabbanan; the klal-prat-klal cascade (54a): בעל הבור ישלם
  re-generalizes → living things; והמת "things subject to death"
  (Rashi: "are vessels mortal?!"); final: כסף ישיב לבעליו — "whatever
  has owners." The per-mitzvah species-list table (54b: Sinai's אם
  includes birds).
- Bavli 112b: document authentication in the party's presence from
  והועד בבעליו (MARQUEE above).
- Yerushalmi BK: 1:1 four-avot sources (keren from OUR וכי יגוף; shen
  and regel both out of ושלח את בעירה via Isaiah). 1:2 — pit-deepening
  chain (dug 10, deepened 1: last for death; Rabbi vs R. Yitzchak's
  emendation on who owns damages); "plaster the pit and ACQUIRE it" —
  שמירת נזקין כשמירת קניין; Sumchos: depth 3 width 4; R. Elazar
  HaKappar's victim-relative pit (MARQUEE above). 2:1 — can ha'adah
  attach to conduct OUTSIDE the body? (wall-toppling forewarned ox:
  cofer without stoning — it was forewarned for WALLS, no man present
  before). 2:6 — R. Meir reads מתמול שלשום as "spread gorings"; open
  cases: 3 species / 3 days, gap-day tolerance debated via the NIDDAH
  skipped-examination dispute (Rav Adda vs Rav Huna: vadai vs safek) —
  the state machine's gap-tolerance argued through purity law. 3:1 —
  joint tortfeasors: ox pushed ox into pit — R. Natan: mu'ad half/
  half; tam: ox-owner 3/4, pit-owner 1/4 (the apportionment table;
  Tosafot 13a defends the arithmetic); stone-placer liable for the
  person, exempt for the flask, unless he HURLED. 4:2 — pursuit-
  counter (MARQUEE above). 4:4 — forewarned-before-guardian vs
  before-owner; borrowed-as-tam-found-mu'ad: owner half, borrower
  half; returned before verdict → exempt (R. Yaakov: even after
  verdict, before stoning). 4:5 — slave DAMAGES: "the addendum shall
  not exceed the principal" vs "pays full damage." 4:6 — two-agent
  homicide decomposition in cofer terms (first struck a dying blow,
  second scrambled him — who pays cofer, who damages, worked under
  both nizak- and mazik-valuation); R. Hoshaya "father of the
  Mishnah": the verse teaches cofer-AFTER-death (inheritance rule);
  sold-ox-found-gorer: Rav mekach taut, Shmuel "I sold it for
  slaughter." 4:7 — R. Yudan exempts ownerless from damages too, BUT
  "for COFER all agree liable" (R. Hoshaya; ruled in practice). 5:6-
  5:8 — one verse feeds both death-bor and damage-bor; hefker-in-
  public question ("may one disown his damages in public domain?");
  INVERTED vessel rule: the DAMAGE-pit (under 10) is liable for
  vessels, only the death-pit excludes them (k"v ת"ל structure);
  Shmuel: air-death exempt, floor-impact liable — R. Yochanan + Resh
  Lakish: even impact exempt, "the Torah exempted the manner of
  falling." 6:1 — "no guarding written in its BODY except horn."
- Rashi rows: the tam/mu'ad split might have been read as DETACHED-
  horn only (Zedekiah's strapped irons) — kml natural horn too; snake
  executed IN SKILAH "like the man-killing ox"; keren-from-body means
  the VICTIM eats any shortfall; pesulei-hamukdashin: pit-exempt
  (carcass unownable) yet goring-liable (redeemed = רעהו); children
  in pits exempt purely by decree (no contributory argument); the
  prone first-tripper is MAZIK on his body (even vessels) but BOR on
  his load.
- Tosafot rows: tam-in-man can't sit among the avot (pays from body;
  "all avot pay from the best"); why bor/esh pay no cofer — עליו ולא
  על בור ואש; bor's shor-lo-adam still needed to exempt a fallen
  SLAVE; woman-ribbui needed wherever איש is written (R. Tam:
  nagicha-death would have imported שור איש's exclusion).
- Odds: BM 27a — "chamor of bor per R. Yehudah and seh of aveidah —
  difficult for everyone" (the stray-word audit). BB 93a — pregnant
  cow gored, fetus found dead beside her, timing unknown → HALF
  damage on the cow, QUARTER on the fetus: doubt split into money.
  Yad Ramah BB 3a: partition-wall "lechatzot" idiom borrowed from
  וחצו את כספו; BB 26a: the gramma essay — nezikin learns species-
  rules from SHABBAT (shor-shor) as licensed cross-domain transfer.
  Ben Yehoyada 78b: damages to hekdesh exempt mid'oraita (שור רעהו)
  but liable MIDRABBANAN for tikkun ha'olam (the priests-who-
  disqualified mishnah) — his resolution of Rava's stolen-offering
  case.
- Ledger: 3,872 → 3,965. Remaining: 760 readable + 6 tanakh.

## Bite 6 (batch 6) — 96 listings: THE RAMBAM STRATUM + SANHEDRIN/MAKKOT/GITTIN ROWS + YERUSHALMI SANH/GITTIN/ORLAH + ODDS
- MT Damages to Property (the codified machine): liability grounded on
  כי יגף (1:1); keren/shen/regel WITH toledot taxonomy inside the ox —
  and the tail-wagging DOUBT case (excessive wagging: keren-toledah or
  regel? → safek; a victim who SEIZES half keeps it). Tam/mu'ad
  defined by DEVIATION vs custom (המשנה); the five tam-acts; born-
  mu'ad five + snake; "here is the damager before you, take it even if
  worth a dinar" (1:3); the right-of-way matrix incl. joint yards BY
  DESIGNATION (fruit-yard vs beast-yard, 1:9). Ha'adah before owner
  AND court (6:2); stadium oxen (6:5); moserah ruled like R. YEHUDAH
  (7:1 — tam pays, mu'ad exempt); assessment/depreciation/
  appreciation-split codified with the worked 120-carcass example
  (7:8-7:10); carcass-hauling duty (7:13). Hekdesh exempt, meilah-
  kodashim have NO nezikin, pesulei hamukdashin DO (8:1); hefker ox:
  first seizer WINS, post-fact hekdesh/hefker exempts (8:4). ALL
  species stoned, all victims incl. slaves; GENTILE victim exempt "as
  per their laws" (10:1, Kiryat Sefer: bein/bat/eved/amah listed →
  goy excluded); cofer = Heaven-death redeemed AND seized by force
  despite being atonement (10:4); terefah rationale: "its owners are
  as dead, needing no death" (10:7; vs Rava in Sanh 78a: a terefah OX
  that killed IS liable — only the terefah-OWNER's ox exempt; Rav
  Ashi extends exemption — the B1 TT row's dispute localized). Cofer
  = VICTIM's value (11:1, dmei-nizak codified); flat slave-30;
  me'ukav-get NO fine. Pit codified 12:1-13:1: WOOL-FILLED pit still
  liable (the air kills); hefker-domain lattice (rashut alone →
  liable; rashut+pit or pit-alone hefker/hekdesh → exempt);
  duty-to-fill = digging; CAMEL-PROOF cover standard (occasional
  camels → liable; none local → ones); impaired-victim rule (sound
  beast by day = ones → death-exempt; a MAN always death-exempt, even
  blind, even at night); startle-fall OUTSIDE the pit: court doesn't
  collect but SEIZURE STANDS (12:18); vessels exempt (13:1).
- Rambam satellites: Forbidden Foods 4:22 — on verdict the ox "becomes
  like an impure species"; kosher-slaughter after verdict still
  banned; ZOMEMIM-REVERSAL CODIFIED: exempt discovered before stoning
  → back to the herd, after stoning → permitted in benefit (the
  Keritot rule). Foreign Worship 4:12 — condemned-CITY beast = stoned-
  ox analog; executed woman's hair permitted, her WIG is spoils
  (Yerushalmi Gittin 6:5: "let my clasp go to my daughter").
  Marriage 5:2 — kiddushin with its DUNG valid ("not important
  relative to the ox"). Sacrifices Unfit 6:1 — live admixture never
  nullified ("living beings are important"). Sheqel Dues 1:2 — the
  slave-30 coin spec: 320 barleycorns raised to 384 (Bayit-Sheni
  sela). Sefer HaMitzvot: Neg 188 (not to eat its flesh), Pos 237
  (judge beast-damages) + bailee mitzvot.
- Sanhedrin sugyot: the Yannai summons in situ (19a); Ben Yehoyada's
  layer — "stand ON YOUR FEET" = no leaning; "before Him who spoke and
  the world was" = the true judge as God's partner in creation;
  Gabriel's SLAM (חבטה = 24 = the permutations of אדני which is
  דינא); measure-for-measure: they flattered sitting, died slammed.
  78a: Rava — terefah ox liable, terefah-owner's ox exempt; zomemim
  on a terefah's killer not executed ("not within refuters-of-
  refuters"). 79b: convicted ox mixed with unconvicted — rabbanan all
  exempt (verdict in its presence); R. Yehudah: CONFINE THE HERD in a
  kippah. Rashi 16a: only the king's OX needs 23 (his other property
  — ordinary courts).
- Makkot 2b: ZOMEMIM who fabricated a mu'ad pay the COFER per the
  dmei-mazik view; "sold for his THEFT, not for his refuted plot."
- Gittin 42a-b: half-slave (MARQUEE above); me'ukav-get kenas question
  in situ. 49a + Tosafot + Yerushalmi Gittin 5:1: the hekdesh-k"v
  sugya — Yerushalmi: "damages to the commoner, NONE to the Most
  High" (נזקין להדיוט ואין נזקין לגבוה); pledge-payer pays Temple
  from BEST land; and the victim's LIEN on the tam's body SURVIVES
  SALE (owner sold the gorer → "its body was already encumbered to
  the victim"; Caesarea rabbis: unless converted to a loan).
- Yad Ramah BB 175b: pit-digger dies in his own pit as an ox falls on
  him — the ox exempt, and the digger's HEIRS pay the ox's value:
  oral obligations collect from the estate, proved from בעל הבור
  ישלם.
- Oath grid (Shevuot 36b + Yerushalmi 5:6): "your ox killed my ox" —
  denial-oath → liable; "killed my SLAVE" → exempt (fine, pays-more-
  than-damage); Yerushalmi asks whether the whole 30 is fine or only
  the excess ("even a boil-afflicted slave draws 30" → all fine) and
  knots the son-case against both cofer-valuations.
- Odds: Bekhorot 9b — the stoned ox still conveys FOOD-impurity;
  Bekhorot 49b/Rashi 51a — the tariff coinage harmonized (where
  "shekel" is unwritten, learned via "fixed money"); Temurah 28b —
  gorer vs rove'a mutually irreducible (cofer only in one); Temurah
  30b — flesh forbidden, dung permitted vs idolatry's "cherem like
  it"; Yerushalmi Orlah 3:1/Pesachim 2:1 — R. Yochanan: a POULTICE of
  stoned-ox flesh draws no lashes ("its prohibition isn't clarified");
  the braita reconciled by owner-slaughtered-before-verdict; Ben
  Yehoyada Sotah 35a — Uzzah's על השל read through our יכרה (dug);
  Kiryat Sefer 6:6 — a mu'ad SOLD or GIFTED reverts to TAM (change of
  domain resets the state); Chagigah 4a — the shoteh defined by the
  mu'ad-for-all template (MARQUEE above); Niddah 8a — the stoned
  rooster (MARQUEE above).
- Ledger: 3,965 → 4,061. Remaining: 664 readable + 6 tanakh.

## Bite 7 (batch 7) — 46 listings: TARGUMS WHOLE + MITZVAH-COUNT LAYER (SEFER HaMITZVOT / SMaG / CHINUKH) + MT SLAVES/ALTAR + DIVREI DAVID (TAZ)
- MT Slaves 3:14: the ha'anakah floor = 30 sela pegged to OUR slave-
  fine (MARQUEE above); grant only from blessed-by-themselves goods
  (flock/threshing-floor/vat), not coin or clothing; leaves-by-
  redemption gets nothing ("he was not SENT free — he paid").
- MT Altar-Forbidden 4:3: stadium killer-ox altar-kosher, "as one
  coerced" (MARQUEE above); rove'a-disqualification age thresholds.
- Sefer HaMitzvot: Neg 188 (eating its flesh = lashes, even kosher-
  slaughtered post-verdict); Pos 237/238 (ox-law, pit-law as counted
  court-mitzvot); Shorashim 8:5 — the לא-disambiguation essay
  (MARQUEE above).
- SMaG Pos 66/68 + Neg 135: the pit corpus codified with ALFASI's
  ruling — halakha like Rabbah AND like R. Akiva, so bor liable BOTH
  in public domain and in his-domain-where-he-freed-the-ground-but-
  not-the-pit; every left obstacle = bor-toledah, mafkir nezakav
  CHAYAV (R. Yochanan over R. Elazar his student); wool-sponges
  negate impact; mound-vs-pit; the impaired-victim table; civic
  infrastructure law: no hollows under the public road (even
  wagon-proof — "lest the roof sink unknowingly"), digging FOR the
  public permitted, no beams over the road unless above camel+rider,
  the road-swap rule ("what he gave he gave, what he took he did not
  take"); the CHASID coda (MARQUEE above; Ravina: Avot; others: the
  blessings).
- Chinukh 51/53: "all the justice-mitzvot share one root — an
  intelligible matter" (דבר משכל); bor named only for the 10-tefach
  death-standard.
- ONKELOS whole span: ואף מרה יתקטל (owner "killed" — Minei Targuma
  defends: rabbinic kattla covers Heaven-death, "who doesn't learn is
  chayav kattla"); אם ממון ישוון עלוהי (cofer rendered MONEY); bein/
  bat = בר/בת ישראל; 30 SELA'IN; 21:35 "the VALUE of the dead they
  split" (R. Yehudah's money-split in translation).
- Minei Targuma 21:30 (essay): Onkelos' mammon vs the sugya's
  cofer=atonement; Ramban — the cofer is atonement one cannot be
  DISTRAINED for (hence conditional אם), vs Rambam 10:4 who rules
  distraint from the unresolved BK 40a; MT's structural read of that
  sugya: R. Acha b. Yaakov's distraint-question DEPENDS on the
  partners-question (the conditional אם proves a no-cofer case
  exists = the partners), which is why R. Nachman said "I am shut in
  by the FIRST."
- TARGUM JONATHAN whole span: the six inlined rulings (MARQUEE above);
  plus 21:28 owner clear "of death AND of slave/maid-value" — two of
  the three tannaitic נקי readings compiled into one clause.
- Divrei David (Taz on Rashi): shor-shor-from-Shabbat mechanics; the
  לא-יאכל sugya with the ben-pekuah objection resolved ("even where
  its stoning IS its slaughter, the verdict forbids"); against
  Mizrachi — the braita does hold like R. Abbahu, נקי comes for the
  HIDE. Why Rashi omits crouching from the keren-toledot (small-
  vessel crouching is regel per R. Elazar). The והמית-ribbui gives
  TOLEDOT-of-keren cofer (else עליו ולא על האדם might swallow them).
  On Rashi's "אם here is not conditional": the mandatory-אם list
  omits ours because it RIDES the mamona/kappara dispute — and Rashi
  compared אם כסף תלוה rather than ואם מזבח because OUR אם is
  vav-less like it (orthographic selection of the comparandum). The
  kids-clause needed against the pit-style counter-sevara ("adults
  should watch where they walk"). The flat-30 glossed "gezerat
  hakatuv" HERE (not in Arakhin) because here the free-man verse
  would otherwise contradict. The long defense of Rashi's pit-
  homiletic (Rabbah vs Rav Yosef on whose-domain the Torah's pit is;
  the tzerikhuta held by all; the 9+1 finisher-rule surviving via
  איש אחד ולא שנים).
- Ledger: 4,061 → 4,107. Remaining: 618 readable + 6 tanakh.

## Bite 8 (batch 8) — 105 listings: RASHI COMPLETE + GRAMMAR ROWS + LEKACH TOV WHOLE + MIDRASH AGGADAH + TANCHUMA + SEKHEL TOV + DIVREI DAVID TAIL
- Rashi on the span (canonical layer): common-case species; לא יאכל +
  נקי midrash AND peshat (the peshat: נקי must be said of the TAM
  because the mu'ad-verse "kills" the owner); והועד = warning-
  language (from Judah's העד העד בנו); והמית ribbui for bite/push/
  kick; bidei shamayim; אם not conditional; cofer valuation — Rashi's
  Mekhilta attribution: dmei NIZAK = R. Yishmael, dmei MAZIK = R.
  AKIVA (the attribution FLIP vs the Bavli's R. Yishmael b. R.
  Yochanan b. Beroka = mazik; Lekach Tov matches Rashi); flat 30 =
  gezerat hakatuv + the Cologne conversion (MARQUEE above); pit =
  UNCOVERING a covered one; digger-after-digger; cover exempts,
  public-domain speaker; species via shor-shor-from-Shabbat (Divrei
  David defends this route against Tosafot's kesef-yashiv route, and
  answers why the Mishnah's all-beasts list omits GORING — the bor
  ribbui certifies the gezerah shavah, goring inherits); בעל הבור =
  "owner of the STUMBLING-BLOCK — Scripture made him its owner to be
  liable" (Divrei David builds the shor-pikeach/adam split on this:
  liability tracks the tekalah-owner where causation holds, adam-
  exempt is pure decree); the LONG 21:35:3 essay — the halving-verse
  speaks only of EQUAL oxen; from the equal you learn the unequal
  (tam = half, never profit, never stricter-than-mu'ad); the halving
  PHRASING exists to teach body-only payment ("the victim loses" on
  a shortfall).
- Rashi grammar rows (MARQUEE above) + Berakhot 27a: the stoned
  rooster "pecked the FONTANEL of an infant" — the soft-spot detail.
- LEKACH TOV whole span: opens by SHOWCASING the shor-shor gezerah
  shavah as one of the 13 middot — "see how beloved is Torah... the
  sages who searched and expounded will receive good reward," and
  "whoever doubts the words of the sages is judged in boiling
  excrement"; the rooster as the attested case. FIVE נקי readings
  compiled (hide/blood/fat via את; R. Yehudah b. Beteira: clear in
  HEAVEN's court; half-damage; RSbG: slave-fine; R. Akiva: fetus-
  money, with the ox-aimed-at-man-struck-pregnant-woman case). The
  five differences; R. Meir vs R. Yehudah with "Scripture supports R.
  Yehudah"; moserah per R. Meir with "our Mishnah follows R. Yehudah
  — search and find" (בלוש ותשכח). The Bavel enforcement note + the
  stone-clearer parable (MARQUEE above). Mazal = ומוראכם (fear-of-man
  upon beasts — the beast lacks it toward its fellow). רעהו excludes
  nokhri, KUTI, and ger; kids/slaves/women — "their striking is bad"
  both ways. R. Akiva's equal-oxen limit: "we never find victims
  collecting more than their damage"; the "half that isn't half"
  wordplay (from Isaiah's חציו שרף).
- Midrash Aggadah: the theft-verse (21:37) rows arrive as dual-anchor
  — חמשה בקר masculine / צאן feminine, and the JOSEPH CIPHER: the ox
  = Joseph (בכור שורו), the TEN MARTYRS killed for his sale ("you
  shall be sold to your enemies") — the ox-theft verse as the
  Joseph-sale ledger. Noah's-ark-as-cofer (MARQUEE above).
- Tanchuma Buber rows: the golden-calf tariff (MARQUEE above); איך
  אשיתך as liability-setting; the mishpatim homily (the angel sent
  when Israel became liable — Moses refused him, Joshua fell on his
  face; "twice I came").
- Sekhel Tov: Jacob's ויחץ (halving his camp before Esau) glossed
  from OUR וחצו את כספו — the patriarch's split described with the
  ox-halving verb; כריתי = dug/bought (R. Akiva's sea-towns).
- Midrash Mishlei 22: שלישים read via מתמול שלשום — the block's
  "three days" cited in the everything-is-threefold homily (Torah/
  Prophets/Writings, אמת's letters, the third month...).
- Ledger: 4,107 → 4,212. Remaining: 513 readable + 6 tanakh.

## Bite 9 (batch 9) — 58 listings: IBN EZRA BOTH RECENSIONS + RAMBAN + SFORNO + RADAK ROWS + PRINTED TANCHUMA + MIDRASH TANNAIM + SHEMOT RABBAH
- Ibn Ezra (both recensions): the ANTI-VICTIM-BLAMING rationale — the
  woman is named because in some places women don't frequent the
  ox-fields ("lest one say SHE deviated from custom"); the boy/girl
  named "lest one blame the parents for not guarding them — were he
  grown he'd have fled." ולא יאכל peshat: the owner may have
  slaughtered not knowing it gored. יומת read as literal desert
  commuted by ransom ("like eye-for-eye: he OUGHT to die unless he
  gives his redemption" — riding on יומת vs ימות); no clash with לא
  תקחו כופר — THAT is a full murderer, this one only failed to guard
  (tied badly, gate left open). The 30 = "price of a MIDDLE slave in
  those days" (market-rate theory); the Karaite deflection recorded
  ("the deniers say a Hebrew slave — five shekels per year of six");
  slave "from any nation, Canaanite not far-fetched." BEN ZUTA again
  (21:35): the Karaite read רעהו as the ox's fellow — "the ox has no
  fellow except Ben Zuta alone." Morphology rows: ישמרנו assimilation
  (MARQUEE above); בעלים plural-of-lordship (Isa 16:8, 26:13); Lev
  27:16 — the barley-field valuation called "the King's decree LIKE
  THE SLAVE-PRICE" (two statutory flat rates).
- Ramban: the יומת philology — capital law always doubles (מות יומת);
  bare יומת = Heaven; then TWO defenses of Onkelos' יתקטיל ("he
  deserves killing but ransom stands," or Heaven executes BY THE
  SWORD — "his day will come, or he goes down to war and perishes");
  Onkelos tracks R. Akiva on the zar. Cofer = uncoerced atonement (no
  distraint, no compulsion to court — hence אם; vs Rambam 10:4 who
  rules distraint). The kids-clause peshat: an ox that kills a GROWN
  man is "like a bereaved bear" — warned-and-unguarded is gross
  negligence; children's killer less indicative → הו"א exempt, kml
  not. The pchat-neveilah CORRECTION of Rashi (21:34): the carcass-
  clause isn't payment-in-kind (he could pay in bran!) — it makes the
  carcass the VICTIM's property from death, so post-mortem
  depreciation/theft falls on him. 21:36: the two guarding-doctrines
  (mu'ad needs SUPERIOR guarding vs equal-guarding-greater-fault) read
  into ולא ישמרנו; והמת יהיה לו workable for victim OR damager — same
  law either way. Crossrefs: Gen 9:5 flood-covenant (MARQUEE above);
  Deut 20:8 — Bahag counts ולא ימס as a lav "in the manner of ולא
  יאכל את בשרו" (the lo-ambiguity theme from B7's Shorashim, argued
  from the OTHER side); Exod 30:23 — מר דרור glossed "free of
  adulteration, as in ובעל השור נקי" (the ox's clean-verdict idiom
  naming pure myrrh).
- Sforno: the two verses as EVIDENTIARY BRANCHES — וגם בעליו יומת =
  Heaven's court when there are NO witnesses; אם כופר = when
  witnesses testify, the court sets the ransom. And the 30 = the
  FEMALE erekh of Arakhin, "for the slave is like her in
  mitzvah-obligation" — the tariff priced off the woman's valuation
  via the shared mitzvah-profile.
- Radak rows: מגפה defined from our וכי יגף (sudden lethal blow — the
  Enoch essay); the Ps 22 polemic + Ps 40's dug ears (MARQUEE above).
- Printed Tanchuma / Shemot Rabbah: the איך אשיתך complex — God as
  prosecutor SETTING liability from אם כופר יושת עליו (Shemot Rabbah:
  "you obligated YOURSELVES — ככל אשר יושת עליו"); the matron's-son
  orchard parable; the golden-calf 30-shekel version with God
  POINTING: "THIS they shall give" (the fire half-shekel). Tanchuma
  Mishpatim 7: the chok list (MARQUEE above). Shemot Rabbah 10:2: the
  plague of pestilence read via our וכי יגף ("Behold I am NOGEF");
  frogs drawing the Egypt/Kush border ("your border — not others'");
  Chananiah/Mishael/Azariah's k"v from the oven-frogs.
- Midrash Tannaim Deut 5:14: the REVERSE gezerah shavah — SHABBAT's
  ox-and-donkey species-scope learned FROM our damages verse (R. Yosi
  in R. Yishmael's name) — the transfer running opposite to the
  Bavli's shor-shor-from-Shabbat.
- Ledger: 4,212 → 4,270. Remaining: 455 readable + 6 tanakh.

## Bite 10 (batch 10) — 61 listings: CHIZKUNI WHOLE + TUR (HaArokh, CM 389 + 410) + RABBEINU BAHYA WHOLE + KITZUR BAAL HaTURIM + BEKHOR SHOR
- Chizkuni: the tam-then-mu'ad puzzle — if the tam dies after its
  first kill, how does a killer-mu'ad exist? It FLED TO THE MARSH
  after early gorings, or "they know the owner but not WHICH ox"
  ("you have a goring ox in your herd" — the unidentifiable
  defendant). נקי = "so long as it was not forewarned." Cofer: the
  heirs' consent frames the court's power (MARQUEE above). The
  kids-clause blocks victim-blaming ("she's a gadabout... the father
  didn't guard them — his words are NOTHING"). Slave-goring must be
  MU'AD (else the slave's claim outranks the free man's). The 30 =
  female erekh 20-60 (לה-לה from the woman). Pit scenarios: יפתח = a
  long-finished pit; יכרה = fresh dig left open overnight "because he
  means to return to work tomorrow." Wagon-cover standard from the
  Yerushalmi. The exclusions RATIONALIZED: man has daat (he lost
  himself), vessels "don't travel without a human guard" — against
  the pure-decree school. בעל הבור necessarily = tekalah-owner ("the
  land-owner committed no fault"). The halving JUSTIFIED: a tam
  neither owner could foresee — "the MAZAL OF BOTH caused it,
  therefore they share the loss equally." Gen 9:5: מיד כל חיה closes
  the indirect-murder loophole ("let no one say: I'll throw my enemy
  among the beasts"). Num 35:31: cofer valid for limbs and
  Heaven-deaths; only the murderer barred.
- Kitzur Baal HaTurim: the gematria battery (MARQUEE above) + נגח 2x
  in the Masorah (death→damages for minors); לבעליו 3x — the third is
  "wealth kept for its owner TO HIS HARM: from his wealth he dug a
  pit in the public domain"; המת יהיה = "the owners attend the
  carcass" in gematria.
- Tur HaArokh: Ramban's Onkelos discussion imported; cofer
  non-distraint; bereaved-bear peshat; and the Tur's OWN
  defective-spelling drash on בר ("defective, and no other"): even a
  non-complete digger — the 9+1 finisher — is liable (a Tur ancestor
  of the Gra's vav-machine, B2).
- Tur Choshen Mishpat 389: the slave-daat moral-hazard rule codified;
  NO MU'AD TODAY — forewarning needs ordained judges, so every ox
  stays tam forever, and ox-that-killed isn't judged (needs 23) — the
  kenas-tefisah regime governs (seized half-damage isn't returned).
  The born-mu'ad five: Rambam (full damage in ALL modes) vs R"I —
  each predator is mu'ad only in ITS characteristic mode (a lion
  clawing-and-eating is its way; killing-then-eating is DEVIANT =
  tam-horn) — predator ethology parsed into the lattice; Rosh sides
  with R"I. WORKERS entering to claim wages: license turns on whether
  the master frequents the market — and ROSH: "nowadays the custom is
  universal that workers enter the house, and no one carries coin at
  market — so liable regardless" (living custom updates the
  license-default). The joint-yard designation lattice; the resting
  cow ("walking over her is your right; kicking her is not").
- Tur CM 410: pit = stationary-property damage — even SPILLED WATER
  on the road is a bor; duty transfers between partners by handing
  the COVER (public well: by handing the BUCKET); the first digger's
  grace window = "know it + hire workers + CUT CEDARS" — and Ramah:
  from "cut" (not "buy") — if cedar sells only overpriced he may WAIT
  for a fair price (procurement law inside tort law); negligence
  TRANSFERS across causal paths (negligent re camels → liable when it
  worm-rotted, since THIS ox was fated to fall either way); the
  water-layer arithmetic (9 + 1 water = 10 and liable; 5+2, 7+3
  unresolved → exempt); multi-digger shares (8+1+1 all liable per
  share; 9+1 finisher alone; un-digging the extra tefach → unresolved
  → both exempt, tefisah holds); ox-pushes-ox codified (mu'ad
  half/half; tam quarter — and TODAY the quarter is an uncollectible
  fine NOT shifted to the pit-owner); the man+ox+pit push-matrix
  (fetus-damages: man alone; vessels: man+ox, pit exempt); digger
  killed by the falling ox → his HEIRS pay the ox (the Yad Ramah row
  now in the code); Ramah's collection-cap on joint tortfeasors vs
  the Tur's critique.
- Rabbeinu Bahya: nagicha = PROVIDENCE, negifa = chance (mazal as
  hashgachah); the stoning per Ramban's deterrent-peshat; then the
  serpent/satan filing (MARQUEE above) + "in Talmudic times the Satan
  appeared visibly until they prayed for his concealment"; the
  chasid-nezikin + stone-clearer retold; pdyon from Job 33:24
  ("deliver him from the pit — I have found a RANSOM"); the
  cherem-verse bars only the murderer; "even a pearl-piercing slave,
  even a boil-stricken one — 30"; Benjamin's 300 (MARQUEE above); the
  EIGHT DEGREES OF TZEDAKAH essay rides in on the mandatory-אם list
  (our cofer as one of the three obligatory אם's).
- Bekhor Shor: ולא יאכל even to gentile/dogs; נקי via the mu'ad-verse
  contrast (Rashi's peshat) + his superfluity note; והועד = "they
  warned him TO GUARD and he didn't"; the heirs'-option peshat + the
  release-to-kill murderer (MARQUEE above).
- Ledger: 4,270 → 4,331. Remaining: 394 readable + 6 tanakh.

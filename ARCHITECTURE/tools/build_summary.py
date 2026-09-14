#!/usr/bin/env python3
"""build_summary.py — the program at block grain: where it breaks, what each block does.

The breaks are the scroll's own weekly portions (parashot). They are used
here because the code's operator mix changes at them: the Genesis blocks
are dominated by acts, commands, and results (world-building and record);
Mishpatim and the Leviticus blocks by cases, handlers, and statutes (law
installation); Terumah and Tetzaveh by specification steps with almost no
operators (a building spec); Vayakhel and Pekudei by the spec executed; the Numbers blocks
(added 2026-09-13) by the acts run and the laws installed together.
The per-block operator counts below are computed from the frozen units;
the plain-English bullets are written by hand from the units' own titles,
state summaries, exports, and compiled functions.

Read-only over the repository. Writes ONLY ARCHITECTURE/program/SUMMARY.md
and SUMMARY.html.

    python3 ARCHITECTURE/tools/build_summary.py
"""
import html, os, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_program_outline import OUT, cw

# block -> (book, span, mode, [units...], [bullets...], compiled)
BLOCKS = [
 ("Genesis", "Bereshit", "1:1-6:8", "builds the world, then records the first cases",
  ["gen_01","gen_02","gen_03","gen_04","gen_05","gen_06","gen_07","gen_08","gen_09","gen_10","gen_11","gen_12","gen_13","gen_14","gen_15"],
  ["Boots the world in seven ledger days: a clock, two containers (heaven and earth), light, sky, land and seas, plants, the lights, the creatures, humanity. Each day is commanded, built, tested, named, and committed. Day seven's transaction is left open.",
   "Installs the first rule (the tree) and traces the first violation: the rule misquoted, the eating, the sentences, the exile.",
   "Records the first offerings, the first murder and its sentence, the first city and crafts, and the death ledger of Adam's line down to Noah.",
   "Opens the flood: the stolen verdict, the hundred and twenty years, the decree."], None),
 ("Genesis", "Noach", "6:9-11:32", "executes a building spec, then installs the first law for everyone",
  ["gen_16","gen_17","gen_18","gen_19","gen_20","gen_21","gen_22","gen_23","gen_24","gen_25","gen_26"],
  ["Takes the ark as a specification (dimensions, decks, door), then runs it: the boarding with its dates, the rise, the remembering, the waters going home, the exit and the altar.",
   "Installs the blood law with the blessing: be fruitful again, but no blood, and life for life. The first standing law binding all humanity.",
   "Sets the covenant of the bow as a standing handler: the bow in the cloud, and God remembers.",
   "Records the vineyard curse, the table of nations, Babel's build and its halt, and Shem's ledger down to Terach."], None),
 ("Genesis", "Lech Lecha", "12:1-17:27", "opens promises as demands that stay open",
  ["gen_27","gen_28","gen_29","gen_30","gen_31","gen_32","gen_33"],
  ["Records the call and the journey, and opens the land and seed promises as demands on the ledger. They stay open through the whole book.",
   "Records the descent to Egypt, the separation from Lot, the war of the kings, and the priest's blessing.",
   "Runs the covenant of the pieces (the stars, the four hundred years) and Hagar's angel; installs the law of the flesh (circumcision) and the renamings of Abraham and Sarah."], None),
 ("Genesis", "Vayera", "18:1-22:24", "judgment scenes and a tested demand",
  ["gen_34","gen_35","gen_36","gen_37","gen_38"],
  ["Records the visitors at Mamre, the plea for Sodom with its bargaining count, the overthrow, the pillar, the cave.",
   "Runs the Gerar dream-court: the prophet's prayer, the shut wombs; then Isaac's birth, the expulsion, and the well-oath.",
   "Records the binding as a test and closes it with the oath: the seed as stars, the gate of enemies."], None),
 ("Genesis", "Chayei Sarah", "23:1-25:18", "transactions with receipts",
  ["gen_39","gen_40","gen_41","gen_42"],
  ["Records the Machpelah purchase as a complete transaction: price weighed, witnesses at the gate, the deed's language. The tradition's source for acquisition by money.",
   "Runs the servant's oath and the well test, the retelling, the release, and the betrothal; then Abraham's end and Ishmael's line."], None),
 ("Genesis", "Toledot", "25:19-28:9", "contracts, a switched blessing, a mismatched party",
  ["gen_43","gen_44","gen_45","gen_46","gen_47"],
  ["Records the twins and the birthright sale; Isaac in Gerar with the sister-claim, the hundredfold, the wells, and the covenant swear.",
   "Records the hunt-command and the blessing delivered to the wrong party. The machine flags it: the demand's addressee and its performer do not match.",
   "Records Esau's grudge, the flight order, and the sending to Paddan."], None),
 ("Genesis", "Vayetze", "28:10-32:3", "wages, vows, and a household ledger",
  ["gen_48","gen_49","gen_50","gen_51","gen_52","gen_53","gen_54"],
  ["Records the Bethel ladder, the name written on the place, and the first vow, opened as a demand.",
   "Runs the wage of seven years and the switched bride; the opened wombs and the twelve name-writes with their reasons; the speckled-wage contract and the peeled rods.",
   "Records the return-command, the flight over the river, the pursuit and search, and the heap of witness named in two tongues."], None),
 ("Genesis", "Vayishlach", "32:4-36:43", "names written, deaths ledgered",
  ["gen_55","gen_56","gen_57","gen_58","gen_59"],
  ["Records the two camps and the gift, the wrestled name (Israel written), the blessing returned to Esau, and the first altar.",
   "Records the deceit at the gate: nine demands made, none performed. Then Bethel again, three deaths on the road, and Esau's ledger of chiefs and kings."], None),
 ("Genesis", "Vayeshev", "37:1-40:23", "a pledge that speaks; demands opened and forgotten",
  ["gen_60","gen_61","gen_62","gen_63"],
  ["Records the dreamer sent, stripped, and sold.",
   "Records Judah and Tamar: the pledge taken as evidence, the levirate duty, the verdict reversed by the pledge itself.",
   "Records Potiphar's house (the refusal, the false charge) and the two dreams in prison, with the petition that is forgotten."], None),
 ("Genesis", "Miketz", "41:1-44:17", "a famine run as a state machine",
  ["gen_64","gen_65","gen_66"],
  ["Records Pharaoh's dreams and Joseph's rise: the seven-year plan, the storing, the selling.",
   "Records the first descent (the brothers before the governor, the money returned in the sacks) and the second (Benjamin brought down, the meal, the cup planted)."], None),
 ("Genesis", "Vayigash", "44:18-47:27", "an open transaction closes",
  ["gen_67","gen_68","gen_69","gen_70"],
  ["Records Judah's surety speech, the unmasking, and the brothers' guilt resolved.",
   "Records the descent of the seventy, Goshen, and the fifth: Joseph's economy over Egypt, land and persons."], None),
 ("Genesis", "Vayechi", "47:28-50:26", "testaments, and the oath left open",
  ["gen_71","gen_72","gen_73"],
  ["Records the crossed hands (the blessing routed past the elder), the testament of the twelve, and the coffin in Egypt.",
   "Leaves one oath open for Exodus to close: the bones to be carried up."], None),
 ("Exodus", "Shemot", "1:1-6:1", "the population, and the call",
  ["exo_01","exo_02","exo_03","exo_04","exo_05"],
  ["Records the names, the midwives (the first open demands of the book), the child drawn from the water, the bush and the Name, the signs and the firstborn, and bricks without straw."], None),
 ("Exodus", "Va'era", "6:2-9:35", "a scripted run with repeated calls",
  ["exo_06","exo_07","exo_08","exo_09"],
  ["Records 'I am the LORD' and the genealogy that seats Moses and Aaron.",
   "Runs the plagues as repeated calls of one script: warning, execution, result. Staff and blood, frogs, lice, swarms, pestilence, boils, hail."], None),
 ("Exodus", "Bo", "10:1-13:16", "the code's first statute book",
  ["exo_10","exo_11","exo_12","exo_13"],
  ["Records locusts, darkness, and the last warning.",
   "Installs the first statute book: the calendar's zero ('this month'), the lamb and its registration, the leaven window with its karet, the access filter (who may eat), the firstborn consecrated and redeemed, the telling to the child."],
  "cold_run_pesach.py 24/24"),
 ("Exodus", "Beshalach", "13:17-17:16", "narrative with law seeds",
  ["exo_14","exo_15","exo_16","exo_17"],
  ["Records the sea split, the Song, Marah's waters.",
   "Records the manna, and with it the Sabbath's first rules: the double portion, the boundary, no gathering. Then Massah and Amalek."], None),
 ("Exodus", "Yitro", "18:1-20:23", "institutions installed",
  ["exo_18","exo_19","exo_20"],
  ["Installs the courts: Jethro's tiers of judges, the hard cases sent up.",
   "Records the covenant at Sinai and installs the Ten Utterances with the case law their own words carry: the vain Name, the Sabbath clauses, theft, the altar rules."],
  "cold_run_decalogue.py 12/12"),
 ("Exodus", "Mishpatim", "21:1-24:18", "the law code proper",
  ["exo_21","exo_22","exo_23_justice","exo_23_escort","exo_24"],
  ["Opens the cases and installs their rules: the Hebrew slave's six-year clock and the pierced 'forever', the maidservant's three rights, homicide and the place of asylum, injuries and their five payments, the goring ox's two states, the pit, theft and its multiples, the four guardians, the seducer's fine, the lender and the pledge.",
   "Installs the court ethics, the sabbatical year, the weekly rest, the three feasts, the first fruits, the kid clause.",
   "Records the angel escort and the conquest bounds, the covenant blood, and the forty days."],
  "cold_run_mishpatim.py 23/23 + cold_run_mishpatim_2.py 9/9; cold_run_guardians.py 12/12; cold_run_calendar.py 14/14"),
 ("Exodus", "Terumah", "25:1-27:19", "a building specification",
  ["exo_25","exo_26","exo_27"],
  ["Specifies the ark, the table, the menorah, the curtains, the boards, the veil, the screen, the outer altar, the court. Almost no operators fire here: the block is measurements and types.",
   "Those measurements are constants other laws import later: the court's hundred by fifty becomes the Sabbath carrying limit; the hangings become a boundary line in a lashes statute."], None),
 ("Exodus", "Tetzaveh", "27:20-30:10", "specification of persons and rites",
  ["exo_28","exo_29"],
  ["Specifies the lamp's oil, the priestly garments (ephod, breastpiece, robe, frontplate, tunics), the seven-day investiture with its offerings, the daily offering, and the incense altar."], None),
 ("Exodus", "Ki Tisa", "30:11-34:35", "the run breaks and is repaired",
  ["exo_30","exo_31","exo_32","exo_33","exo_34"],
  ["Installs the census shekel, the laver, the anointing oil and the incense; names the craftsmen; sets the Sabbath as the sign.",
   "Records the break: the calf, the tablets broken, the Levites, the plague, the tent pitched outside.",
   "Records the repair: the favor, the glory shown, the thirteen attributes, the second tablets, the covenant renewed, the shining face."], None),
 ("Exodus", "Vayakhel", "35:1-38:20", "the specification executed, piece by piece",
  ["exo_35_shabbat","exo_35_36","exo_37","exo_38"],
  ["Puts the Sabbath first, then records the freewill gifts (too much brought) and the craftsmen called.",
   "Records every piece built as specified: curtains, boards, veil, ark, table, menorah, incense altar, oil, bronze altar, laver, court."], None),
 ("Exodus", "Pekudei", "38:21-40:38", "the inventory and the commit",
  ["exo_39","exo_40"],
  ["Records the metals inventory, the garments made, and all the work brought and blessed.",
   "Records the erection on the first month, the anointing, the glory filling the tent, the cloud guiding. The machine is handed to Leviticus running, not halted."], None),
 ("Leviticus", "Vayikra", "1:1-5:26", "procedures as functions",
  ["lev_01","lev_02","lev_03","lev_04","lev_05"],
  ["Installs the offering procedures: the ascending offering from cattle, flock, and bird; the grain offering in its five forms; the peace offering with the fat and blood ban.",
   "Installs the sin offering as a tree of four ranked cases (priest, congregation, leader, commoner) with zero statutes and one procedure each.",
   "Installs the graded guilt offering (the witness, the impurity, the oath, with three tiers by means), misuse of sancta, and the deposit oath's restitution: principal, a fifth, and the ram."],
  "cold_run_vayikra5.py 27/27; cold_run_offerings.py 40/40 (the Lev 1-8 dispatcher)"),
 ("Leviticus", "Tzav", "6:1-8:36", "the priests' law layer, and an installation transaction",
  ["lev_06","lev_07","lev_08"],
  ["Installs the perpetual fire, the vessel purge (earthenware broken, copper scoured), the griddle offering's halving, the rejection machine (out of time, out of place, no permitters), the karet bans, and the priestly dues.",
   "Runs the seven-day installation of the priests as one atomic transaction: no basket, no priesthood; committed at the blood sprinkling; released at day seven."],
  "cold_run_tzav.py 33/33"),
 ("Leviticus", "Shemini", "9:1-11:47", "the first run, then a classifier",
  ["lev_09","lev_10","lev_11"],
  ["Records the eighth-day service and the fire from before the LORD; Nadav and Avihu, the mourning limits, the drink ban, the remaining offerings eaten.",
   "Installs the species classifier: split hoof and cud together, fins and scales, the bird list by name, the locust's joints, the eight swarmers; and the carcass status machine (touch, carry, until evening)."],
  "cold_run_shemini.py 19/19"),
 ("Leviticus", "Tazria", "12:1-13:59", "state machines on the body",
  ["lev_12","lev_13"],
  ["Installs childbirth purity with its durations for a son and a daughter, and the birds for the poor.",
   "Installs the skin-mark intake with its quarantine loop, and the tracks for skin, boil, burn, head and beard, and garment: signs, weeks, released or decreed, burned."],
  "cold_run_negaim.py 16/16 + the ten houses 10/10 (with Metzora)"),
 ("Leviticus", "Metzora", "14:1-15:33", "the cleansing procedures and the house machine",
  ["lev_14","lev_15"],
  ["Installs the leper's cleansing: the two birds, the shaving, the offerings, the poverty branch.",
   "Installs the house affliction: shut, pull, scrape, plaster, and the fork between birds and demolition. Then the male and female discharge purity."], None),
 ("Leviticus", "Acharei Mot", "16:1-18:30", "the service order and the blood center",
  ["lev_16","lev_17","lev_18"],
  ["Installs the Yom Kippur service as an ordered program: the entry limits, the two goats and the lots, the blood sequence, the confession, the eternal statute.",
   "Installs slaughter at the Tent and the blood-is-life ban; the sexual prohibitions and the land that vomits out its inhabitants."],
  "cold_run_yoma.py 18/18"),
 ("Leviticus", "Kedoshim", "19:1-20:27", "a statute register",
  ["lev_19","lev_20"],
  ["Installs the holiness ledger: fifty-six statutes under one card. Parents, the Sabbath, the poor's edges, honest dealing, love your neighbor, mixtures, the stranger, just weights.",
   "Installs the sanctions register: Molech, the medium, the sexual penalties, and the holy people."], None),
 ("Leviticus", "Emor", "21:1-24:23", "who may serve, what may be offered, and when",
  ["lev_21","lev_22","lev_23","lev_24"],
  ["Installs the priests' mourning and marriage limits, the blemished priest, who may eat holy food, and which offerings are acceptable.",
   "Installs the appointed times: the Sabbath, Passover and unleavened bread, the omer and its fifty days, the shofar day, the affliction day, the seven days in booths with the four species.",
   "Installs the lamp and the bread; then records the blasphemer's case, held in custody until the code arrives, with talion as money and one law for sojourner and native."],
  "cold_run_moadim.py 24/24; cold_run_lev24.py 23/23 (exports talion(), called by Mishpatim)"),
 ("Leviticus", "Behar", "25:1-26:2", "clocks on the land: the seventh year and the fiftieth",
  ["lev_25"],
  ["Installs the sabbatical of the land: six years sown, the seventh at rest, and the fiftieth year proclaimed with the trumpet, every man returned to his holding.",
   "Installs the land's inalienability: sold only until the Jubilee, redeemed by a kinsman or by the count of years remaining; the poor brother lent to without interest.",
   "Installs the Hebrew slave's standing (not as a bondman, out at the Jubilee) and the foreign slave's; this is the clause Exodus 21's 'forever' imports to end the pierced slave's service."], None),
 ("Leviticus", "Bechukotai", "26:3-27:34", "the covenant's consequence table, and the valuations",
  ["lev_26","lev_27"],
  ["Installs the blessing and the cascading curse as the covenant's consequence table: walk in the statutes and the land yields; refuse, and seven-fold escalations follow, down to exile; then the remembering of the covenant.",
   "Installs the valuations: a vow of a person priced by age and sex, the animal, the house, the field priced by its seed and the years to the Jubilee, the devoted thing, the tithe of the herd."], None),
 ("Numbers", "Bamidbar", "1:1-4:20", "a census run as arithmetic the machine had to learn to read",
  ["num_01","num_02","num_03","num_04_kehat"],
  ["Runs the count Exodus ordered: twelve tribes by names, twenty years and upward, 603,550 in all — the same number the half-shekel silver gave at the tabernacle's accounts; the Levites exempted from the count and set to guard the tabernacle.",
   "Lays out the camp in four standards around the tent, and fixes the order of the march as the order of the camp.",
   "Counts the Levites by their houses against the firstborn of Israel and prices the excess: 273 souls at five shekels each, 1,365 shekels to Aaron. The Levite houses sum to 22,300 against the written 22,000, the gap the Talmud asks about.",
   "Assigns the Kohathites the holy things under their wrappings, on pain of death for looking, and sets the Levite's working age at thirty to fifty."],
  "cold_run_bamidbar.py 66/66"),
 ("Numbers", "Naso", "4:21-7:89", "work-counts, a purity ladder, two personal engines, and twelve days written into the past",
  ["num_04_gershon_merari","num_05","num_06","num_07"],
  ["Counts Gershon's and Merari's service and sums the three work-counts to the written 8,580; sends the leper, the discharger and the corpse-unclean out of their camps.",
   "Installs the trespass with its added fifth and the priest's gifts, the suspected wife's ordeal with merit as a parameter, and the nazirite's term as a live clock — set at the vow, cancelled at a corpse, re-set from the eighth day.",
   "Installs the priests' blessing as a fixed form, and records the wagons and the twelve princes' offerings, one prince per day, as twelve dues dated a month before the census, the chapter's totals closing at twelve times one prince's gift."],
  "cold_run_naso.py 274/274"),
 ("Numbers", "Beha'alotcha", "8:1-12:16", "the rites run, the march begins, and the tradition's day-table is graded",
  ["num_08","num_09","num_10","num_11","num_12"],
  ["Records the lamps raised and the Levites' cleansing rite run as commanded, with their service age at twenty-five against chapter 4's thirty — and Chronicles' twenty, with its reason.",
   "Records the Passover kept in the first month — a date earlier than the book's opening — and the unclean men's case: the halt, and the second Passover installed as a rule for the generations, its due computed by the calendar.",
   "Installs the two silver trumpets and records the departure from Sinai on the twentieth of the second month; the three days' journey, the month of quail and Miriam's seven days run as timers against the Talmud's own day-table.",
   "Records Taberah, the graves of craving, the seventy elders with Eldad and Medad, and Miriam struck and shut out — the camp's halt a debt the text closes when she is brought in."],
  "cold_run_beha.py 154/154; cold_run_pesach_sheni.py (the tent's second case, Numbers 9)"),
 ("Numbers", "Shelach", "13:1-15:41", "the decree that turns days into years, and a case held in custody",
  ["num_13","num_14","num_15"],
  ["Records the twelve spies sent and returned at the end of forty days, the night of weeping, the intercession, and the decree: a day for a year, forty years — the timer set here fires in the fortieth year.",
   "Installs the libation table for the land, the dough offering, the stranger's one law, the offerings of the community and the individual who err, and the high hand's cutting off.",
   "Records the wood-gatherer found on the Sabbath and held in custody because the manner of death had not been declared; the answer installs stoning into the Sabbath law of Exodus; then the fringes."],
  "cold_run_shelach.py 172/172; cold_run_mekoshesh.py 34/34 (the tent's third case)"),
 ("Numbers", "Korach", "16:1-18:32", "a rebellion run on undated days, and the priesthood's standing dues",
  ["num_16","num_17","num_18"],
  ["Records Korach's assembly, the censers' test 'tomorrow', the earth's mouth and the fire — Korach's own death an open row, the text naming him at one verse and not the other.",
   "Records the plague stayed by Aaron's incense at 14,700, and the twelve staffs with Aaron's budding, kept beside the manna jar in the same formula.",
   "Installs the priests' and the Levites' watch — 'no more wrath' is chapter 1's clause with one word added — the twenty-four gifts as a covenant of salt, the firstborn's redemption at five shekels, the tithe, and the tithe of the tithe."],
  "cold_run_korach.py 155/155"),
 ("Numbers", "Chukat", "19:1-22:1", "a purity clock, and the fortieth year arriving on four dates",
  ["num_19","num_20","num_21"],
  ["Installs the red heifer's rite and the corpse's seven days with the third and the seventh as timers; the tent, the open vessel, the toucher of the toucher.",
   "Records Miriam's death at Kadesh, the rock struck twice against the order to speak and the sentence on Moses and Aaron, Edom's refusal, and Aaron's death on Mount Hor with Eleazar invested — dated by the itinerary to the first of the fifth month of the fortieth year — and the thirty days' weeping.",
   "Records Arad's vow, the serpents and the copper serpent on the pole, the well's song, and Sihon and Og: the land east of the Jordan possessed."],
  "cold_run_chukat.py 159/159"),
 ("Numbers", "Balak", "22:2-25:9", "the seer's chapters read as a run, and the zealot's rule installed by a deed",
  ["num_22","num_23","num_24","num_25"],
  ["Records Balak's call, the she-ass and the angel, the three stands and the four parables — the curse asked for turned to blessing, every altar's burnt offering called into the offerings engine.",
   "Records Peor: the whoring after Moab's daughters, the judges' sentence, Zimri and Cozbi, Phinehas's spear and the plague stayed at 24,000 — the zealots' rule installed on the tent by the deed, with no halt and no docket; the covenant of peace; the command against Midian left open."],
  "cold_run_balak.py 105/105"),
 ("Numbers", "Pinchas", "25:10-30:1", "the world counted again, a case that fixes the inheritance, and one speech made one table",
  ["num_26","num_27","num_28","num_29"],
  ["Runs the second census after the plague — 601,730 by the same reader — into a population table only a rule may write, tribe by tribe and family by family, the changes declared and not explained: Simeon's loss beyond the plague is labeled; no man of the first roll is left save Caleb and Joshua; the land is to be divided by lot and by the names.",
   "Records the daughters of Zelophehad: the judgment brought near, the inheritance order installed for the generations, their holding left open to Joshua; Moses shown the land and Joshua commissioned.",
   "Installs the offerings calendar as one table — the daily lamb, the Sabbath's, the new moon's, Passover's, the firstfruits', Tishri's three days, Sukkot's declining bulls and the eighth day — eight recurring debts on the altar keyed to the calendar's own words."],
  "cold_run_second_census.py 70/70; cold_run_zelophehad.py 55/55 (the tent's fourth case); cold_run_musafim.py 110/110"),
 ("Numbers", "Matot", "30:2-32:42", "a law in Moses' voice, a war that pays old debts, and a conditional grant",
  ["num_30","num_31","num_32"],
  ["Installs the vows: a man bound by his own word; a daughter's or a wife's vow confirmed by silence on the day of hearing or annulled that day — the hearing day the engine's own timer — and the late annulment charged to the husband.",
   "Records the war on Midian as the run of three open debts: Balaam and the five kings slain, the vessels purified by the tradition's analogy with Leviticus 11, the spoil halved and tributed one in five hundred and one in fifty, the officers' gold in the half-shekel's own words.",
   "Records Gad and Reuben's request, Moses' rebuke and the doubled condition — the tradition's source for the law of every condition — the grant given from now with the crossing left open to Joshua, the cities built, and Machir, Jair and Nobah."],
  "cold_run_vows.py 147/147; cold_run_midian.py 99/99; cold_run_gad_reuben.py 74/74"),
 ("Numbers", "Masei", "33:1-36:13", "the record of the run, the land's extent, and the book's last law",
  ["num_33","num_34","num_35","num_36"],
  ["Records the itinerary of forty-two stations written at the run's end, with Aaron's death dated to the day and the judgments on Egypt's gods told here alone; then the command to dispossess and to destroy the figured stones, its negative arm a warning.",
   "Installs the land's four borders as one status on the land, the lot cited and not rewritten, and the twelve dividers named as rows in the population table.",
   "Installs the Levites' forty-eight cities with their two thousand cubits and the six cities of refuge: the murderer's table by instrument, manner and intent; the manslayer's term until the death of the high priest — an entry closed by a death, not a timer; the two witnesses; no ransom; and the land that blood pollutes. The book closes on the words it opened with, 'in whose midst I dwell'.",
   "Records the tribe's second plea about the daughters, answered without a halt: they marry within their father's tribe, and the book's commands close in the plains of Moab."],
  "cold_run_journeys.py 53/53; cold_run_borders.py 56/56; cold_run_refuge.py 51/51; cold_run_zelophehad.py (36:1-12)"),
]

COUNT_OPS = {"EVENT": "acts", "DECLARE": "commands", "RESULT": "results", "PRECONDITION_STATE": "standing facts",
             "REGISTRY_INSTALL": "world entries", "NAME": "names", "COMMIT": "day commits", "CASE": "cases",
             "HANDLER": "rules", "STATUTE": "statutes", "WITNESS_READ": "shelf readings", "WITNESS_STATE": "shelf readings"}


def main():
    units = dict(cw.frozen_units_in_canonical_order())
    manifests_dir = os.path.join(os.path.dirname(os.path.dirname(HERE)), "logic", "oral_audit", "manifests")
    import json
    rows = []
    for book, name, span, mode, prefixes, bullets, compiled in BLOCKS:
        uids = [u for u in units if any(u.startswith(p) for p in prefixes)]
        c = collections.Counter(); n_steps = 0; n_claims = 0
        for u in uids:
            d = units[u]
            for s in d.get("boot_steps") or []:
                n_steps += 1
                for o in s.get("operators") or []:
                    k = COUNT_OPS.get(o.get("op"))
                    if k:
                        c[k] += 1
            p = os.path.join(manifests_dir, u + "_claims.json")
            if os.path.exists(p):
                m = json.load(open(p, encoding="utf-8"))
                n_claims += len(m.get("claims") if isinstance(m, dict) else m)
        rows.append((book, name, span, mode, uids, bullets, compiled, n_steps, c, n_claims))

    def countline(n_steps, c, n_claims, uids):
        order = ["acts", "commands", "results", "standing facts", "world entries", "names", "day commits",
                 "cases", "rules", "statutes", "shelf readings"]
        parts = ["%d %s" % (c[k], k) for k in order if c[k]]
        return "%d units, %d verses; %s; %d claims checked" % (len(uids), n_steps, ", ".join(parts) if parts else "specification steps, no operators", n_claims)

    last = BLOCKS[-1]
    md = ["# THE PROGRAM AT BLOCK GRAIN — where the code breaks, and what each block does", "",
          "%d blocks from Genesis 1:1 to %s %s, cut at the scroll's own weekly-portion breaks. " % (len(BLOCKS), last[0], last[2].split("-")[-1]) +
          "The breaks are used because the code's operator mix changes at them: Genesis blocks run on acts, commands, "
          "and results (world-building and record); Mishpatim and the Leviticus blocks on cases, rules, and statutes "
          "(law installation); Terumah and Tetzaveh on specification steps with almost no operators (a building spec); "
          "Vayakhel and Pekudei on the spec executed. The counts under each block are computed from the frozen units. "
          "The bullets say in plain words what the block does. Finer grain, one bullet per verse, is in "
          "[PLAIN_OUTLINE.md](PLAIN_OUTLINE.md); the operators as written are in [PROGRAM_OUTLINE.md](PROGRAM_OUTLINE.md).", ""]
    H = ['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
         "<title>The Program at Block Grain</title>",
         "<style>body{font-family:Georgia,serif;max-width:900px;margin:1.5rem auto;padding:0 1rem;line-height:1.55;color:#1e1b14;background:#fbf8f0}"
         "h1{color:#6e5417;border-bottom:2px solid #cdb56a;padding-bottom:.3rem}h2{color:#6e5417;margin-top:2.4rem}"
         "h3{margin:1.6rem 0 .2rem;color:#1e1b14}h3 span{color:#8a6d2f;font-weight:normal}.mode{color:#a33b1f;font-style:italic;margin:0 0 .3rem}"
         ".counts{font-size:.85em;color:#57503f;margin:.2rem 0 .5rem}.compiled{font-size:.85em;color:#2f5d8a}ul{margin:.3rem 0 .6rem}li{margin:.25rem 0}"
         "p.intro{color:#57503f}</style></head><body>",
         "<h1>The program at block grain: where the code breaks, and what each block does</h1>",
         '<p class="intro">%s</p>' % html.escape(md[2])]
    cur = None
    for book, name, span, mode, uids, bullets, compiled, n_steps, c, n_claims in rows:
        if book != cur:
            cur = book
            n_blocks = sum(1 for r in rows if r[0] == book)
            md += ["## %s — %d blocks" % (book, n_blocks), ""]
            H.append("<h2>%s — %d blocks</h2>" % (book, n_blocks))
        md += ["### %s %s — %s" % (book, span, name), "", "*Mode: %s.*" % mode, "",
               countline(n_steps, c, n_claims, uids), ""]
        if compiled:
            md += ["Compiled function: " + compiled, ""]
        md += ["- " + b for b in bullets] + [""]
        H.append('<h3>%s <span>%s %s</span></h3>' % (html.escape(name), html.escape(book), html.escape(span)))
        H.append('<p class="mode">Mode: %s.</p>' % html.escape(mode))
        H.append('<p class="counts">%s%s</p>' % (html.escape(countline(n_steps, c, n_claims, uids)),
                                                  (' <span class="compiled">· compiled: %s</span>' % html.escape(compiled)) if compiled else ""))
        H.append("<ul>" + "".join("<li>%s</li>" % html.escape(b) for b in bullets) + "</ul>")
    H.append("</body></html>")
    open(os.path.join(OUT, "SUMMARY.md"), "w", encoding="utf-8").write("\n".join(md))
    open(os.path.join(OUT, "SUMMARY.html"), "w", encoding="utf-8").write("\n".join(H))
    covered = sorted({u for r in rows for u in r[4]})
    missing = [u for u in units if u not in covered]
    print("blocks:", len(rows), "units covered:", len(covered), "of", len(units), "missing:", missing)
    for f in ("SUMMARY.md", "SUMMARY.html"):
        print("wrote program/%s %d KB" % (f, os.path.getsize(os.path.join(OUT, f)) // 1024))


if __name__ == "__main__":
    main()

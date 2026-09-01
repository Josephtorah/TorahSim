# The Answer Key

How the Mishnah and the Talmud test a machine built from the written Torah.

A tutorial. Written 2026-08-31, the day the method proved itself on the whole book of Genesis.

This book explains one step of a larger project. The larger project turns the written Torah into working computer logic, verse by verse, with every line traceable to its source. This book is not about that derivation. It is about what happens after: how the Oral Torah, the Mishnah and the Talmud, becomes the exam that the machine must pass.

Read it to learn the method. Teach it to show anyone what the two Torahs are, in terms a modern person already understands: code, tests, and an answer key.


## Part 1: The machine, in one page

Start with what already exists, because the exam only makes sense against it.

Every verse of Genesis has been read at the level of its own ink: its words, its grammar, its accents, even its spelling. Each verse became a small piece of logic. An event that happened. A command issued. A state that holds. A name written into a registry.

The pieces are honest in a specific way. Nothing enters the logic without a source. Every operator cites the grammar rule or the read source that licensed it. The whole world of Genesis folds into a database with a fingerprint, a hash, and that fingerprint must not move unless the logic itself legitimately changes.

So there is a program. It knows that the waters lifted the ark. It knows the flood's dates. It knows who begot whom, which blessings were said, which names were written one way and read another.

Here is the question this book answers. That program was built from the written text alone. The Jewish tradition says the written Torah always traveled with an oral companion. If that is true, the oral companion should have something to say about our program. It should be able to test it.

It does. And the test has a shape that any software engineer will recognize instantly.


## Part 2: The two shelves

The oral library splits into two kinds of books, and the split decides everything about how we use them.

**Verse-anchored books** start from the verse and walk toward the meaning. The midrash collections work this way. So does Onkelos, the ancient Aramaic translation. These books are organized like our machine: Genesis 1:1 first, then 1:2, then 1:3. You can read them alongside the text. In the project they are called the reading shelf, and they feed the derivation itself.

**Case-anchored books** are different. The Mishnah, the first great written code of Jewish law, does not walk through verses at all. It is organized by topic, into 63 tractates: Shabbat for the Sabbath laws, Yevamot for family law, Chullin for food law. Open a page and you will not find a verse commentary. You will find a case.

A case looks like this. A rockslide falls on a person on the Sabbath. May you dig? A man has two sons and no daughters. Has he fulfilled the command to be fruitful? The wheat was sold as good and turned out bad. Who may cancel the sale?

Input, then output. Situation, then verdict. Usually no reason given, and almost never a verse.

That format should sound familiar. It is a test suite. Each Mishnah paragraph is a test vector: given these inputs, the correct output is this. In the project these books are called the testing shelf, and the Mishnah is the answer key. Its tractate structure is even a module map: the tradition already organized the law into topics, so our code organizes itself into the same modules.

**The Talmud is the bridge between the two shelves.** The Mishnah states a verdict and hides its work. The Talmud takes the verdict and asks, again and again, one question: from where do we know this? In the Talmud's own Aramaic the question is one word, מנלן (menalan, "from where do we know it?"). The answer, over and over, is a verse. The Talmud walks the case-anchored ruling back to the verse-anchored text.

So the pipeline is: the written Torah is the program. The Mishnah is the test suite. The Talmud is the traceability report that connects each test to the lines of the program it exercises.

That is not a metaphor invented for this project. It is a plain description of how the three layers actually behave, and this book will show it happening on real examples.


## Part 3: The exam comes first

The method has a strict order, and the order is the whole discipline. It was proven on a pilot of ten cases and then on a full sweep of every remaining Mishnah passage that cites Genesis: 51 rows in total across the whole Mishnah.

**Move 1. Quote the exam before writing any code.** Every case is copied from the Mishnah into a spec file first: the input situation, the expected verdict, the dispute if the Mishnah records one, and a bridge column noting whether the Talmud walks this verdict back to one of our verses. The answer key is fixed before the engine exists, so the engine can never quietly bend the test to fit itself.

**Move 2. Classify every case against the machine as it stands.** Three grades.

Class A: the machine can already answer. Its logic produces the verdict.

Class B: the machine holds the rule as text, a claim seated on some verse, but cannot yet apply it. It knows, but cannot compute.

Class C: the machine holds nothing. The verdict is the Mishnah's own addition.

The pilot's score was honest and telling: A zero, B seven, C three. The reading had seated the law as text. The case shelf is what makes it runnable.

**Move 3. Gaps become findings, never quick fixes.** Every Class C, every partial holding, goes into an append-only findings queue. Nothing is patched on the spot. The owner rules on each finding: seat it in the corpus, import it as a labeled guest, or reject it. This protects the machine from silently absorbing whatever the exam happens to say.

**Move 4. Compile and re-run.** Each Mishnah topic becomes a rule function. A rule takes a case as input and returns a list of verdicts. A dispute returns every side, labeled by its authority, and that is a correct answer, never an error. Every verdict carries its full pedigree: the Mishnah row, the Talmud bridge, the Genesis anchor, and the machine claim that holds it, or an explicit label saying the piece was imported.

**Move 5. The vocabulary is discovered, not designed.** Every input value a case can use is registered with the source that introduced it, quoted in the source's own Hebrew with English beside it. The rockslide is מַפֹּלֶת (mapolet, "a collapse"). The doubtful newborn is סָפֵק (safek, "a doubt"). A case cannot be stated in vocabulary no source ever defined. That is the guard rail against the simulator drifting into invented law.

**Move 6. Pose a case.** A small program walks you through the registered menus, takes your hypothetical, and returns the verdicts with the full pedigree attached. It is the first working cell of the eventual simulation: state a situation in the tradition's own words, hear the tradition's own answer.

**Move 7. When checking what the machine holds, look everywhere it writes.** The corpus holds knowledge in three layers: formal claims, witness rows in the database, and the prose inside operators. The pilot's one blind spot was a dispute that had been sitting in operator prose for a week while the exam searched only the claims. Now every holdings check searches all three layers. A report of absence is only worth the coverage statement above it.

Those are the seven moves. Now watch them run.


## Part 4: The rockslide

The best single example in the whole project. It shows the composite function, the bridge, and a gap being found and repaired.

**The exam row.** Mishnah Yoma 8:7 rules: if a rockslide falls on a person on the Sabbath, and it is doubtful whether anyone is under it, doubtful whether they are alive, even doubtful whether the buried person is someone the law obligates you toward, you clear the debris anyway. If you find them alive, you keep clearing. If you find them dead, you stop.

Three branches. Doubt: dig. Alive: keep digging. Dead: stop.

**What the machine already held.** The reading of Genesis had seated a claim on Genesis 7:22, the verse describing who died in the flood: "all in whose nostrils was the breath of the spirit of life." From that verse the tradition fixes where life is tested: at the nose. The claim even carried the operational detail from the Babylonian Talmud, tractate Yoma 85a: digging from below, you continue until you reach the nose; from above, reaching the nose suffices.

Stop and look at what kind of thing that verse contributed. Not a story. A definition. The verse defines the predicate: what counts as alive, and where you measure it.

And the machine had verified something remarkable at derivation time. The Hebrew construct נִשְׁמַת (nishmat, "breath of") appears in the entire Torah exactly twice. Genesis 2:7, where God breathes life into the first man's nostrils. Genesis 7:22, where that breath is taken from all flesh. The verse where breath is given and the verse where breath is taken are one formula. The tradition built its rescue law on the second, and the machine can show why it could: those are the only two places the definition lives.

**The composite.** Now count what the Mishnah's little rule actually composes. The life-at-the-nose predicate, from Genesis. The Sabbath labor prohibitions, from Exodus. The principle that saving a life overrides the Sabbath, which the Babylonian Talmud derives in Yoma 85b from verses in Leviticus and Exodus. And the doubt logic: stacked uncertainties do not weaken the override.

Four functions, four sources, one test row. No single verse contains the rockslide rule. The composition is the Mishnah's contribution. Each Mishnah row is a composite function, taught by worked example: input and output shown, work hidden. The Talmud is where the work is shown.

**The gap.** When the exam ran, two branches graded Class B: the machine held the doubt rule and the keep-digging rule as text. But the third branch, found dead, stop clearing, was held nowhere. The Sabbath is not desecrated for the dignity of the dead. The override exists for life only, and its boundary is part of the rule.

That became finding F-001. It sat in the queue until the owner said seat it. Then it entered the corpus properly: a claim on the Genesis 7:22 unit, a witness note beside the rescue-law operator, a changelog line, a revision bump, and every automated gate rerun to green. The world's fingerprint did not move, because a witness note is knowledge about the world, not a change to it.

**The honest labels.** Ask the engine the rockslide case today and every verdict names its sources. The doubt verdict cites the Genesis claim. The stop-clearing verdict cites the new claim and says it entered through the exam. And the pedigree carries one more line, called anchor_pending: the override's strongest derivation for doubt cases stands on Leviticus 18:5, "and live by them," and Leviticus 18 has not been derived yet. The machine says openly: this piece of my answer rests on a verse I do not yet contain.

That line is the frontier ledger, and it turns every gap into a signpost. The books not yet derived already owe the engine specific verses, listed with the passage that will pay them.


## Part 5: The machine computes its own answers

Two cases went beyond matching the answer key. The machine derived the answer from its own contents, end to end.

**The flood's twelve months.** Mishnah Eduyot 2:10 rules that the judgment of the generation of the flood lasted twelve months. A lookup engine would store "twelve months" and recite it. This engine does something better.

The Genesis reading had installed the flood's dates as facts. The rain began in year 600 of Noach's life, month 2, day 17. The earth was dry in year 601, month 2, day 27. When the exam asks the duration question, the engine reads its own date rows and computes: twelve months, plus ten days. It reports the excess too, and the tradition itself explains those ten days as the solar year's eleven-day surplus over the lunar. The Mishnah's twelve-month verdict, derived from the corpus's own facts, with the three database rows named in the answer.

**The thirteen covenants.** Mishnah Nedarim 3:11 quotes Rabbi Yishmael: great is circumcision, for thirteen covenants were cut over it. Thirteen is a claim about ink. The project has a standing law about numeric claims: they are never accepted unopened. So the machine opened Genesis 17, the covenant chapter, and counted the covenant word בְּרִית (berit, "covenant") in the chapter's own text.

The count is exactly thirteen. Verses 2, 4, 7 twice, 9, 10, 11, 13 twice, 14, 19 twice, and 21. Rabbi Yishmael's number is not a flourish. It is a census of the chapter's tokens, and the engine now performs that census live, every time the question is asked.

These two cases matter for teaching because they answer the natural skeptic's question: is the machine just parroting the Mishnah? No. Where the sources supply operands, the machine computes, and where its computation matches the tradition's stated verdict, both are confirmed at once.


## Part 6: Disputes are answers, not errors

Modern software treats disagreement as a bug. The tradition treats recorded disagreement as part of the law. The engine follows the tradition.

**The two houses.** Mishnah Yevamot 6:6 asks when a man has fulfilled the command to be fruitful and multiply. The House of Shammai says two sons. The House of Hillel says a son and a daughter, quoting Genesis 5:2, "male and female He created them." Ask the engine about a man with two sons and no daughters and it returns both verdicts, each labeled with its house. For a man with a son and a daughter the houses agree, and the engine returns one verdict noting the agreement.

**The seas and the ritual bath.** Genesis 1:10 reads: "and the gathering of the waters He called Seas." The Hebrew for gathering is מִקְוֵה (mikveh), and that same word is the legal term for a ritual immersion pool. Mishnah Mikvaot 5:4 hangs a three-way dispute on our verse. Rabbi Meir: all seas qualify as a mikveh, for the verse names them a gathering. Rabbi Yehudah: only the Great Sea, the Mediterranean, because the plural "Seas" marks many kinds within one. Rabbi Yosei: seas purify as flowing water, yet are invalid for certain higher purities. Three readings of one naming, all returned, all labeled.

**A dispute about when a law began.** Genesis 32:33 is the only place in Genesis where the narrator states a standing law: "therefore the children of Israel eat not the sinew of the thigh," after Jacob's hip was wrenched in the night wrestling. Mishnah Chullin 7:6 records a dispute about that law's own birthday. Rabbi Yehudah holds it was binding from the sons of Jacob onward. The sages answer with a sentence that every student should memorize: בְּסִינַי נֶאֱמַר אֶלָּא שֶׁנִּכְתַּב בִּמְקוֹמוֹ, "it was said at Sinai, but written in its place." The law was given later and the text seated it here, at the story that explains it.

The machine already carried provenance disputes about facts. Now it carries a provenance dispute about a law's effective date, returned as two labeled verdicts. Disagreement, recorded with its authorities, is a first-class output of the system because it is a first-class feature of the source.


## Part 7: How the links work

The deepest question a student will ask: if the rules pull verses from all over the Bible, what connects them? The tradition has a formal answer, and it turns out to be machine-friendly.

**A worked link.** Mishnah Chullin 5:5 discusses the law against slaughtering an animal and its young "on one day." What is one day: does a day run from morning to morning, or from evening to evening? Ben Zoma answers with a verbal analogy. The phrase יוֹם אֶחָד (yom echad, "one day") appears in the slaughter law, and the same phrase appears in the creation account: "and there was evening and there was morning, one day." In the work of creation, the day follows the night: evening is written first. Therefore in the slaughter law too, the day follows the night. Night plus its following daytime are one legal day.

Look at the mechanics. The link is made by shared ink: the same phrase standing in two verses. The tradition has a name for this move, גְּזֵרָה שָׁוָה (gezerah shavah, "a verbal analogy"), and it is one of the thirteen formal inference rules by which the law is derived from the text. The project records these rules, the middot, on every claim where the source itself argues by one.

**Links live on edges, not in verses.** Genesis 1:5's own logic never changes because of Ben Zoma. The verse still says what it says: evening, morning, one day. What exists now is a link: from Genesis 1:5, to Leviticus 22:28, type verbal analogy, source Ben Zoma, in Mishnah Chullin 5:5. The verse is a node. The inference is an edge. A rule is a named bundle of edges. This is the design of the whole future system: the verses never call each other; the recorded links between them carry the law.

**And the links are discoverable.** Here is the discovery that closed this chapter of the project, stamped by the owner as the biggest news yet. If links run on shared ink, a machine can search for them. The word data behind our texts is morphologically tagged: every word carries a lemma, a dictionary identity. Searching by lemma finds every place a definition's exact words recur, with none of the false matches that plague text search. Which brings us to the scan.


## Part 8: The scan: one definition's career across the whole Bible

The question was simple. The nose verse gave the rescue law its definition of life. Do the other books of the Bible ever use that definition? Is there a function out there that looks like the Mishnah's?

The scan searched all the books for the breath word, נְשָׁמָה (neshamah, "breath"), by its lemma, and for the nose word, אַף (af, "nostril"), by its lemma. Morphology matters: plain text search had matched תִּנְשֶׁמֶת (tinshemet), a lizard in Leviticus's list of creeping things, and a similar word meaning desolation in the prophets. The lemma search excluded the impostors and self-tested by confirming it fires on the two Genesis anchor verses.

Twenty-four verses in the whole Bible carry the breath word. They sort into four postures of a single function.

**The definition, stated.** Isaiah 2:22: "cease from man, whose breath is in his nostrils." A human being is the breath at the nose; that is the predicate, stated as a sentence. Job 27:3 runs it as a condition: "as long as my breath is in me, and the spirit of God is in my nostrils." That is a while-alive clause, in poetry.

**The function called as a selector.** Deuteronomy 20:16 commands, in the wars of the land: "you shall not leave alive anything that breathes," כָּל נְשָׁמָה (kol neshamah, "any breath"). That is Genesis 7:22's flood selector, everything with the breath of life, reused verbatim as the scope of a law. Joshua 10:40 and 11:11 through 14 execute it in the same words.

**The function run as a test.** First Kings 17:17: the widow's son sickens until "no breath was left in him." The narrative declares death by performing the test: check for breath, find none, pronounce dead. Then Elijah revives him. And Second Kings 4:35 is the reverse entry: the boy Elisha revives comes back to life by sneezing seven times. Life returns through the nose. The tradition itself connects this to Genesis 2:7: the soul departs and returns by the door it entered.

**The function revoked.** Job 34:14 and 15: if God gathered to Himself His spirit and His breath, all flesh would perish together. The flood operator, stated in general form: withdraw the breath, and everything dies.

Now say what this means, because this is the teachable heart of the whole book.

The books of the Bible demonstrate the function: they state the predicate, call it, test with it, revoke it. The Mishnah compiles the demonstrations into one executable rule: rockslide, Sabbath, check the nose, three verdicts. The Talmud links the compiled rule back to the verse that defines its terms.

Demonstrate. Compile. Link. Three layers, three jobs, one function, measured end to end in an afternoon. And because the linking runs on shared ink, the machine can propose candidate links by scanning lemmas, while the tradition's recorded inferences confirm which links the chain actually made. The system's growth law follows: a definition seated in Genesis accumulates call sites as every later book is derived.


## Part 9: The honesty rules

The method only demonstrates anything because of the rules that keep it honest. Teach these alongside the results, because they are what separates this project from a machine that merely dresses up in sources.

**Every verdict carries its pedigree.** The Mishnah row, the Talmud bridge, the verse anchor, the machine claim. If a piece was imported rather than derived, the pedigree says imported, names the owner's ruling that allowed it, and states what verse would be needed to derive it properly.

**Silence is honest.** Pose a case no compiled rule matches and the engine says so: the machine is silent, nothing is guessed. A wrong answer would be a failure; a confident invented answer would be worse.

**Numbers are never trusted unopened.** Any claim about counts, spellings, or written forms is checked against the ink itself. The thirteen covenants passed that check. Claims that fail such checks are recorded as failed, per source, per claim, because a source that is wrong once is not thereby wrong everywhere.

**A report of zero is worth only the coverage statement above it.** Any scan that reports an absence must first prove it can find the thing it is looking for. The project relearned this the hard way during this very sweep: a probe searched case-sensitively for "world to come," missed a claim that spelled it in capitals, and briefly declared missing a ruling the machine had held all along. The finding was corrected at the seat, and the correction is on the record. The lesson: an unfalsifiable clean report is not a clean report.

**Findings go through a queue, and stamps survive amendment.** Nothing the exam surfaces is patched on the spot. It is queued, ruled on by a human owner, seated through the normal path with every gate rerun, and the affected units join a re-affirmation queue. Approved work stays approved; the record shows exactly what was added afterward and why.

**The exam can be wrong, and the text wins.** In the pilot, the engine flagged a case where the exam spec itself had misstated the House of Shammai's position. The Mishnah's plain text adjudicated: the engine was right, the exam was corrected, and the correction note stays visible. Even the answer key is accountable to the source.


## Part 10: What the full exam measured

The numbers, for the record and for the skeptic.

The entire Mishnah cites Genesis in 51 places. The pilot examined 3. The sweep read the other 48, every one, from the shelf's own Hebrew.

Of the 48: 25 were material. 12 turned out to be commentary-drawn links where the Mishnah's own text never touches Genesis. 4 were mere word echoes. 7 were liturgy or geography using Genesis facts. 2 were verbatim duplicates, credited after one copy was fully read.

Ten modules now stand compiled: the rockslide override, the procreation measure, the judgment durations, the sciatic sinew, the day boundary, the seas as mikveh, forgiveness after injury, the seed categories, the world-to-come census, and the circumcision third day. Twenty-eight test cases across pilot and sweep. Twenty-eight answered. Zero mismatches.

And the headline, the sentence to lead with when demonstrating the project: the reading anticipated the exam. Nineteen of the twenty-five material rulings were already in the machine before the exam arrived, seated during the verse-by-verse reading, several held in more detail than the Mishnah itself states. The count of ten generations was already a claim. The rainbow's place among the things created at twilight was already a claim. The flood generation's verdict, with all four ways the sages parse its proof verse, was already a claim.

Two layers, written and oral, built by different routes, agreeing at nineteen of twenty-five points before anyone forced them to. That is what the project set out to test, and the exam is how it gets tested, forever, one tractate at a time.

**What comes next.** The Babylonian Talmud cites Genesis in 958 distinct passages. Most are bridges, read when their Mishnah row is tested. Some are law the Talmud derives from Genesis directly with no Mishnah row above it, like the seven laws of the children of Noach, derived in tractate Sanhedrin from Genesis 2:16. Those await their own triage. The frontier ledger lists the verses the engine is owed by books not yet derived: Leviticus 22:28 for the day boundary, Leviticus 18:5 for the life override, and more. Every gap has an address.


## Closing: how to run it, and how to teach it

To run the exam engine yourself, from the project folder: python3 World/step9/pose_case.py

The menus offer only vocabulary a source actually introduced, each choice shown with its Hebrew and its English. Pick a module, state a case, and read the verdicts with their pedigree.

To teach this step, one paragraph is enough to open with.

The written Torah compiles into a program. The Mishnah is its test suite: thousands of input-output cases, organized by topic, verdicts stated with the work hidden. The Talmud is the traceability layer: it asks, of every verdict, from where do we know this, and answers with a verse. We quoted the tests before writing any code, graded the machine honestly, queued every gap for a human ruling, compiled the rules with full pedigree on every answer, and found that the machine built from the written text already contained most of what the oral answer key demands. Where it computed, it computed the tradition's own numbers from the text's own ink. And the links between the layers run on shared words that a machine can find.

The rest is doing it again, book by book, tractate by tractate, with the ledgers open the whole way.

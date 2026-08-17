# THE LETTER SCHEMA AND THE WORD SCHEMA: Sefer Yetzirah beside the morphology layer
2026-08-17 · owner ask: "the morphology and the sefer yetzirah have
similar data structures... compare the formats... to see if you can
find overlap." Texts: Data/sefaria_export/Sefer_Yetzirah and
Sefer_Yetzirah_Gra_Version (both recensions, He+En, fetched
2026-08-17, on the TorahCode shelf as well via tools/fetch_corpus.py).
Morphology measured live in tanakh.sqlite: 305,507 tagged words
(300,679 Hebrew, 4,828 Aramaic). Citations below give the base
recension's chapter:paragraph, with the Gra recension noted where its
numbering differs; every Sefer Yetzirah quote was verified in the
fetched stream, and every corpus number was computed this session.

THE FINDING. The two systems are the same kind of object: a
fixed-schema feature record imposed on a complete symbol inventory.
The morphology layer tags every word of the corpus with a positional
feature vector; Sefer Yetzirah ("Book of Formation") tags every
letter of the alphabet with one. The field TYPES recur point for
point, and at two places the overlap is not analogy but shared
mechanics measurable in the corpus itself: the gender vocabulary is
identical, and the book's binary letter-toggle is physically present
in the pointed text as the דגש ("dagesh," the dot written inside a
letter).

## The two records

THE WORD RECORD (measured). Each tagged word carries a code such as
HVqw3ms, decomposing positionally: language, part of speech, verb
stem, verb form, person, gender, number. The measured inventory:

- Part of speech, 9 classes partitioning all 305,507 words: noun
  145,869 · verb 73,683 · preposition 64,305 · conjunction 57,401 ·
  particle 54,420 · suffix 47,422 · adjective 14,350 · pronoun
  7,691 · adverb 4,298.
- Gender: masculine 130,870 · feminine 31,217 · both 17,424 ·
  common 11,149.
- Number: singular 136,125 · plural 51,725 · dual 2,810.
- Person: third 38,383 · second 11,150 · first 6,961.
- State: absolute 64,898 · construct 58,752 · determined 816.
- Core verb stems, 7: qal 50,813 · hiphil 9,556 · piel 6,565 ·
  niphal 4,143 · hithpael 915 · pual 463 · hophal 415 (all other
  stem codes are rare forms or Aramaic).

THE LETTER RECORD (quoted). The book opens by declaring the
inventory and its schema: עשר ספירות בלי מה ועשרים ושתים אותיות יסוד
שלש אמות ושבע כפולות ושתים עשרה פשוטות ("ten sefirot of nothingness
and twenty-two foundation letters: three mothers, seven doubles, and
twelve simples," 1:2). Every letter then carries per-class features
(a binary toggle and an opposition pair for the doubles, an element
triad for the mothers, a faculty for the simples) and a coordinate in
three realms, named as the book's own witness list: עדים נאמנין עולם
שנה נפש ("faithful witnesses: world, year, soul," 6:1; that is,
space, time, and body).

## The overlaps

1. THE EXHAUSTIVE PARTITION. The morphology's first field splits the
   whole word inventory into 9 disjoint classes by behavior. The
   book's first field splits the whole letter inventory into classes
   of 3, 7, and 12 by behavior, and the split is asserted as
   exhaustive: 3 + 7 + 12 = 22, the complete alphabet (1:2, repeated
   1:10 and 2:1). Both schemas begin with the same move, a total
   categorical type over every symbol in the system.

2. GENDER, THE SAME FIELD WITH THE SAME NAMES. The corpus tagger
   needed a gender column on 190,660 words, with the values
   masculine, feminine, both, common. The book runs the same axis
   through its letters and their products: אש ומים מתחלקים זכר ונקבה
   ("fire and water, dividing male and female," 3:2; the phrase זכר
   ונקבה, "male and female," recurs at 3:5, 3:7, 3:8, and 5:2 in the
   base text). The vocabulary is identical to the grammar's.

3. THE TWO-TONGUES TOGGLE IS IN THE POINTED TEXT. Of the doubles the
   book says: מתנהגות בשתי לשונות ("conducted with two tongues"), and
   the base text at 4:1 prints the toggle itself, letter by letter:
   ב"בּ ג"גּ ד"דּ כ"כּ פ"פּ ר"רּ ת"תּ ("bet and bet-with-the-dot, gimel and
   gimel-with-the-dot..." through resh and tav), glossed תבנית רך
   וקשה ("a pattern of soft and hard"). That dot is the dagesh, a
   real codepoint in our stream, and the grammar's soft/hard toggle
   set is exactly the six letters בגד כפת (b, g, d, k, p, t). The
   book claims SEVEN by including ר (resh), and insists on the count:
   שבע ולא שש שבע ולא שמונה ("seven and not six, seven and not
   eight," 4:2). The corpus itself sits astride the dispute: 19 resh
   tokens in the stream carry the dot (the doubling dot, not the
   soft/hard toggle; the doubled resh is a famous Masoretic rarity),
   so the book's seventh double names precisely the letter whose
   dotting is the marginal case of the whole system. An ancient crux,
   printed by both sides in their own notation.

4. SEVEN-SETS BUILT OF BINARY PAIRS. The core of the verb system is
   seven stems: three active/passive pairs (qal/niphal, piel/pual,
   hiphil/hophal) plus the reflexive hithpael mediating. The tag set
   even writes each passive as a case-flip of its active (p/P, h/H):
   one symbol, two values, distinguished by a toggle. The book's
   engine core is likewise a seven-set of internal binaries: the
   doubles are כפולות שהן תמורות ("doubles that are opposites"), each
   carrying a stated opposition pair (all seven at 4:1): תמורת חיים
   מות ("the opposite of life is death"), תמורת שלום רע ("of peace,
   evil"), תמורת חכמה אולת ("of wisdom, folly"), תמורת עושר עוני
   ("of wealth, poverty"), תמורת חן כיעור ("of grace, ugliness"),
   תמורת זרע שממה ("of seed, desolation"), תמורת ממשלה עבדות ("of
   dominion, servitude"). Two engines, each a seven-member set whose
   members are binary oppositions carried on a single glyph.

5. TRIADS WITH A DECIDING MIDDLE. The book refuses pure binaries.
   The mothers are a balance scale: כף זכות וכף חובה ולשון חק מכריע
   בינתים ("a pan of merit and a pan of liability, and the tongue a
   deciding statute between them," 2:1, repeated 3:1), and
   phonetically: מ"ם דוממת שי"ן שורקת אל"ף חוק מכריע בינתים ("mem
   hums, shin hisses, alef a statute deciding between them," 6:1).
   The morphology schema keeps making the same refusal: number is
   singular/plural with DUAL between them (2,810 words), gender is
   masculine/feminine with the middle values both and common (28,573
   words). Each schema installs a mediator column wherever it draws
   a pair.

6. THE POSITIONAL RECORD. HVqw3ms is one word's complete record:
   seven fields composed in fixed positions. A letter's complete
   record in the book composes the same way: class, toggle or
   element or faculty, opposition pair, and a value in each of the
   three realms (for the doubles at 4:12: seven planets in the
   world, seven days in the year, and שבעה שערים בנפש שתי עינים שתי
   אזנים ושני נקבי האף והפה, "seven gates in the soul: two eyes, two
   ears, two nostrils, and the mouth"). Fixed schema, one record per
   symbol, fields in order.

7. THE COMPOSITION LAYER, WITH ITS COMBINATORICS COMPUTED. Our words
   segment into morphemes on "/" (הַ/נָּהָר, "the/river"): tokens are
   joins of smaller symbols. The book specifies the join operator
   for letters and then counts the join space twice. First the
   pairwise table: עשרים ושתים אותיות יסוד קבועות בגלגל ברל"א שערים
   ("twenty-two foundation letters, fixed in a wheel, in 231 gates,"
   2:4), and 231 is exactly the number of two-letter combinations of
   22. Then the factorial ladder (4:12; Gra 4:16): שתי אבנים בונות
   שני בתים ("two stones build two houses"), שלש בונות ששה בתים
   ("three build six houses"), ארבע בונות ארבעה ועשרים בתים ("four
   build twenty-four houses"), חמש בונות מאה ועשרים בתים ("five
   build one hundred twenty"), שש בונות שבע מאות ועשרים בתים
   ("six build seven hundred twenty"), שבע בונות חמשת אלפים
   וארבעים בתים ("seven build five thousand and forty"), the
   factorials 2 through 7 computed in words, closing צא
   וחשוב מה שאין הפה יכול לדבר ("go out and compute what the mouth
   cannot speak"). The book asserts, with arithmetic, that the
   alphabet is a generative combinatorial system, which is the
   presupposition every morphological tagger operates on.

8. THREE REGISTERS OF ONE CREATION. The opening sentence: וברא את
   עולמו בשלשה ספרים בספר וספר וספור ("and He created His world in
   three books: in writing, in number, and in telling," 1:1). A
   corpus database rediscovers exactly this triple: every row holds
   the written form, the numeric address, and the read layer.

## The misses, printed at full size

- Types versus tokens. The morphology tags 305,507 occurrences in
  context; the same word is tagged differently at different sites.
  The book tags 22 types once, fixed forever. One is a parse of a
  text, the other a schema for an alphabet.
- No person axis. First/second/third person (56,494 tagged words)
  has no analogue anywhere in the book.
- The stipulated columns. The planets, months, zodiac, and organs
  assigned to the letters are correspondences declared by the book,
  not features recoverable from the text, and nothing in the
  morphology answers them.
- Disjoint arities. Nothing in the morphology sums to 22, and no
  partition of it comes out 3/7/12; the 9 parts of speech match no
  letter class.
- The seventh double, both directions. The Tiberian toggle set is
  six letters; the book demands seven. Our 19 dotted resh tokens
  carry the doubling dot, not a soft/hard toggle, so the corpus as
  pointed does NOT give resh two tongues; it merely shows resh as
  the one letter at the boundary of the dotting system. The
  six/seven tension is real and stands.
- Measurement caveats. The dagesh codepoint does triple duty in the
  stream (soft/hard toggle, doubling, and the vowel dot on vav), so
  raw per-letter dot counts overcount the toggle; and the shin/sin
  dot sorts before the dagesh in this database's encoding, so naive
  adjacency scans undercount shin. Both caveats were hit and
  corrected during this session's measurements.

## The projection test: the word record compiled down to the letters

(Added 2026-08-17, on the owner's question: if the morphology defines
a word with an attribute, does that assign the word's letters to
slots of the kind the book provides?) The database aligns its Hebrew
field with its tag field segment for segment across all 305,507
words with zero mismatches, so every prefix and suffix letter
arrives already assigned to its grammatical slot; the inflection
letters inside noun and verb bodies were then tested against what
the tag predicts. Measured realization, attribute by attribute:

- The imperfect verb's person and gender choose its FIRST letter,
  from the set א ("alef," I), נ ("nun," we), ת ("tav," you and
  she), י ("yod," he and they): 26,715 of 26,751 sites, 99.9
  percent.
- The stem chooses a prefix letter: the causative prefix ה ("heh")
  at 100.0 percent of 2,735 perfect sites, the passive prefix נ
  ("nun") at 100.0 percent of 1,414, the derived participle prefix
  מ ("mem") at 99.9 percent of 1,651.
- The perfect verb's person chooses its ENDING letters, the
  suffixes תי ("I did"), נו ("we did"), ת ("you did"), ו ("they
  did"): 96.8 percent of 9,811.
- The masculine plural ends in ים ("the -im ending") at 92.6
  percent; the feminine singular ends in ה or ת at 79.1 percent;
  the reflexive stem shows its ת ("tav") infix at 73.8 percent.

The shortfalls are themselves rules: feminine nouns that carry no
ending (ארץ "land" is feminine bare), and the reflexive's famous
letter swap, the ת ("tav") trading places with a hissing first root
letter (השתמר "guard oneself"). The attribute is not a label
floating over the word; it compiles down to a letter in a position.

Aggregated, 25.1 percent of every letter token in the corpus sits
in a bound grammar slot (36.5 percent counting standalone function
words), and the letters ABLE to hold such a slot are a closed class
of exactly eleven, the grammarians' servant letters: א ב ה ו י כ ל
מ נ ש ת ("alef, bet, heh, vav, yod, kaf, lamed, mem, nun, shin,
tav"). Three letters, פ ס ט ("peh, samekh, tet"), occupy a bound
slot ZERO times in 305,507 words, and four more effectively never.
The morphology, projected downward, therefore partitions the
alphabet itself into operator letters and material letters: a
letter-level classification of exactly the book's genre. But it is
a DIFFERENT partition: the mothers are three for three operators,
the doubles split three operators (ב כ ת) against four material
letters (ג ד פ ר), the simples five against seven. The book
classifies by how the mouth makes the letter, the grammar by what
office the letter can hold.

Three places where the projection lands in the book's own slots:

1. THE NAME-SEAL LETTERS ARE THE MEASURED TOP OPERATORS. Ranked by
   bound-grammar share, the corpus's three chief operator letters
   are ו ("vav," 56.2 percent), ה ("heh," 44.1 percent), י ("yod,"
   43.4 percent). Those three, exactly, are the letters with which
   the book seals the six directions of space, in six permutations
   of the Name: וחתמו ביה"ו ("and He sealed it with yod-heh-vav,"
   1:13, and so through the other five orders for the other five
   directions). The book crowns those letters as the sealing
   operators of the world; the measurement crowns the same three as
   the chief grammatical operators of the text; and with א ("alef")
   they are also the four letters that can fall silent and serve as
   vowels.

2. GENDER IS LETTER-ARRANGED IN BOTH SYSTEMS. The book's crowning
   formula, המליך אות אל"ף ברוח וקשר לו כתר ("He made the letter
   alef king over breath and bound a crown to it," 3:6), is
   per-letter office assignment, the same concept as a servant
   letter holding a grammatical job; and the same paragraph closes
   זכר באמ"ש ונקבה באש"ם ("male with alef-mem-shin, female with
   alef-shin-mem"): gender realized by the ORDER of the same three
   letters. The corpus realizes gender by a POSITIONAL letter, the
   feminine's final ה ("heh"). Different mechanism, same claim:
   gender is stored in the arrangement of the letters, not floated
   above them.

3. THE DIRECTION SLOT. The tag set includes a dedicated suffix for
   direction, the directional ה ("heh," tagged Sd in the database):
   1,080 sites in the corpus, and the carrier letter is ה in 1,079
   of them. It is how the text says its compass: צפונה
   ("northward"), נגבה ("southward"), קדמה ("eastward"), ימה
   ("seaward," which is westward), מעלה ("upward," 111 sites in its
   compounds); and the sweep formula at Genesis 28:14 carries it
   four times in a row, ופרצת ימה וקדמה וצפנה ונגבה ("and you shall
   spread westward and eastward and northward and southward"), each
   compass word tagged with the suffix split off, with the same
   sweep at Genesis 13:14 and Deuteronomy 3:27. The book seals the
   six extremities of space with permutations of יה"ו
   ("yod-heh-vav," 1:13); the grammar, asked how it says direction,
   answers with a bound letter slot whose occupant is ה ("heh"),
   one of those three letters and the measured number-two operator.
   Direction is a letter-realized office in both systems, held by
   the same letter family. One asymmetry, printed at full size:
   five of the book's six axes are so marked, and DOWNWARD is not
   (למטה "downward" keeps its final letter as part of the root,
   outside the slot).

The projection, in short, closes part of the type/token gap listed
above: the tag does reach the letters, a quarter of the text's
letters are slot letters, the class that can hold office is closed
at eleven, and the two systems even name some of the same names.
What the projection does not recover is the 3/7/12 grid itself.

## The system reading

Sefer Yetzirah is, in data terms, a morphology of the alphabet
itself, one level below the corpus's morphology of words: the same
record format (an exhaustive class partition, a gender axis with the
grammar's own vocabulary, binary features carried by a diacritic on
a single glyph, triads with an installed mediator, positional
feature vectors, and a join layer whose combinatorics the book
computes in print). Where the tradition's oral layer has already
entered this project as build instructions, execution log, and
access manual, this book adds a fourth systems document: a claimed
SCHEMA for the writing system underneath everything else, asserting
that the letters are typed, gendered, toggled, coordinatized
records, and that creation proceeded by combining them. The
morphology layer is the schema we recovered from the corpus
empirically; the book is a schema the tradition wrote for the layer
beneath it. They agree on the field types, and they touch
mechanically at the dagesh and at the gender column.

## Boundary

The two recensions differ in paragraph division and wording (base
chapters run 14/6/8/12/4/4 paragraphs, the Gra recension
14/6/9/16/10/7); citations above are to the base text, and every
quoted phrase was verified by probe in both recensions except where
a recension is named. Sefer Yetzirah is late-antique tradition, not
Tanakh: it sits on the shelf as an oral-tradition witness beside the
middot, and no claim is made here about its date or about dependence
in either direction between it and the grammarians. The five
classical commentaries in the bucket (Rasag, that is Saadia Gaon;
Ra'avad; Ramban; HaGra; Pri Yitzhak) are not yet fetched; Saadia's
in particular would bear on the six-versus-seven doubles crux, and
that extension is queued, not run.

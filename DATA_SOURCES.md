# DATA SOURCES — what this repository carries that others wrote, and on what terms

TorahSim's own work — the code, the frozen units, the ledgers, the records — is dedicated to the public domain under CC0 1.0 (see
LICENSE). The texts it reads are other people's work, carried here on their own terms:

- **The Hebrew Bible** (Data/*.xml, and Data/tanakh.sqlite built from them): the Open Scriptures Hebrew Bible (OSHB), the Westminster
  Leningrad Codex with its morphology — https://hb.openscriptures.org — Creative Commons Attribution 4.0. Credit: Open Scriptures.
- **The English Bible** (Data/tanakh_*_jps1917_en.json): the Jewish Publication Society's 1917 translation — public domain.
- **The classical Hebrew library** (the Mishnah, the Tosefta, both Talmuds, the Mishneh Torah, the Mekhilta, the Sifra, the Sifrei, the
  midrashim, the Zohar and the rest under Data/, and the snapshot store torah_grok.SNAPSHOT-main-51801ca.sqlite fetched from the release):
  public-domain works whose digital texts come from Sefaria — https://www.sefaria.org — each under the license Sefaria states for that
  text (public domain, or Creative Commons Attribution / Attribution-ShareAlike / Attribution-NonCommercial). Credit: Sefaria and the
  contributors it names. Nothing here is offered for sale.
- **The shelf** (Data/sefaria_export, not tracked — fetched by `python3 Data/fetch_shelf.py` from Sefaria's public export bucket at
  https://storage.googleapis.com/sefaria-export/): the same terms, file by file, as Sefaria's export states them.
- **Strong's concordance numbers** (Data/strongs_*.json): public domain.

If a text's terms bar the use made of it here, tell the maintainer and it will be removed.

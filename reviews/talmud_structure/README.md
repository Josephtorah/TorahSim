# Talmud structure tools

**Last updated:** 2026-07-19

Living notes and indexes for how Bavli is structured in this repo.

| File | Role |
|------|------|
| [DISCOVERIES_2026-07-19.md](DISCOVERIES_2026-07-19.md) | Pass-by-pass structure findings |
| [cite_index_2026-07-18.json](cite_index_2026-07-18.json) | Scripture citation map `(ויקרא א, ה)` → `Lev.1.5` |
| [cite_index_compact_2026-07-18.json](cite_index_compact_2026-07-18.json) | Cite index; locations capped per ref |
| [operator_index_2026-07-18.json](operator_index_2026-07-18.json) | **All lines** tagged with link/move operators |
| [operator_index_compact_2026-07-18.json](operator_index_compact_2026-07-18.json) | Operator → sample locations + counts |
| [link_phrases_2026-07-18.json](link_phrases_2026-07-18.json) | Catalog of link phrase ids + hit counts |
| [LINK_PHRASES_2026-07-18.md](LINK_PHRASES_2026-07-18.md) | Human-readable list of link words/phrases |
| [SIFRA_TALMUD_LINKS_2026-07-19.md](SIFRA_TALMUD_LINKS_2026-07-19.md) | Sifra↔Talmud parallel catalog (from Mesorat haShas) |
| [LEV1_SIFRA_TALMUD_2026-07-19.md](LEV1_SIFRA_TALMUD_2026-07-19.md) | Lev 1–area subset of that catalog |
| [LEV1_OPENING_MESORAT_2026-07-19.md](LEV1_OPENING_MESORAT_2026-07-19.md) | **First verses of Lev** via MH (early Nedavah → parallels) |
| [ORAL_CODES_WRITTEN_2026-07-19.md](ORAL_CODES_WRITTEN_2026-07-19.md) | How to use MH + Sifra as **coding language** for Written → Pre-Code |
| [LEV_1_2_RESEARCH_2026-07-19.md](LEV_1_2_RESEARCH_2026-07-19.md) | **Lev 1:2 full link research** (Sifra + MH + cite_index + web) |
| [REPORT_lev_1_2_oral_coding_2026-07-19.md](REPORT_lev_1_2_oral_coding_2026-07-19.md) | **Narrative learnings report** (dated; prose summary of Lev 1:2 + MH method) |
| [SOURCE.md](../Talmudic-Logic-Project/SOURCE.md) | Gabbay et al. free PDF (related academic project) |

**Naming (from 2026-07-19):** research/report/index files use `_YYYY-MM-DD` in the name. **On update, rename to today’s date** and fix links. Hubs (`README.md`, `STANDING_DECISIONS.md`, `Agents.md`) stay stable with **Last updated** in body. See `reviews/STANDING_DECISIONS.md` §0.

---

## Standing decision: Mesorat haShas is the parallel index

**We were trying to invent our own global “this Oral place ↔ that Oral place” index.**  
**That already exists.** We do **not** need to rebuild it.

### What it is

**מסורת הש״ס / mesorat ha-shas / “Mesorat haShas”** = traditional **see-also / parallel** links  
(“this spot goes with that spot” — not commentary, not law ranking).

### Where it lives locally

| Location | Role |
|----------|------|
| **`Data/links0.csv` … `links8.csv`** | Full Sefaria-style link dump (~2.5M rows) |
| Column **`Conection Type` = `mesorat hashas`** | **~48,268** parallel edges |
| Our extracts (convenience only) | `sifra_talmud_links_2026-07-18.*`, `LEV1_SIFRA_TALMUD_2026-07-19.md` |

### Why we keep it (and stop inventing a rival)

| Need we had | Answer |
|-------------|--------|
| Sifra unit → Talmud daf | Already in MH (`mesorat hashas`) |
| Global, not one-off | ~48k edges; multi-work network |
| Trustworthy traditional catalog | Printed-page margin tradition + Sefaria dump |
| Rebuild by fuzzy text match? | **No** — wasteful; inherit the map |

**Policy:** Use Mesorat haShas for **where** parallels are.  
Use **our** indexes for **what the line is doing** (verse address, discourse operators) and Pre-Code logic for **rules**.

### What MH links (not only Sifra ↔ Talmud)

Measured on local `mesorat hashas` rows:

| Pair family | ~Count |
|-------------|-------:|
| Midrash ↔ Midrash | 14,141 |
| Talmud ↔ Talmud | 13,014 |
| Midrash ↔ Talmud | 6,028 |
| Tanaitic (Tosefta…) ↔ Talmud | 4,173 |
| Mishnah ↔ Talmud | 3,745 |
| Mishnah ↔ Tanaitic | 1,858 |
| Midrash ↔ Tanaitic | 1,516 |
| Tanaitic ↔ Tanaitic | 1,510 |
| Midrash ↔ Mishnah | 1,271 |
| Mishnah ↔ Mishnah | 941 |

Works include: Bavli tractates, **Sifra**, Mekhilta(s), Sifrei, Rabbah midrashim, **Mishnah**, **Tosefta**, minor Tanaitic works. Tanakh / codes almost never under this type.

### What we still build ourselves (not replaced by MH)

| Index / work | Question it answers |
|--------------|---------------------|
| **cite_index** | Where is **Written verse X** pointed at in Bavli? |
| **operator_index** | What **discourse move** is this Bavli line? |
| **Pre-Code logic units** | What **IF/THEN rules** does the Hebrew support? |
| **ta’amim trees** | How is the **verse** structured? |

Mesorat haShas = **address book of Oral parallels**.  
Our logic work = **what the text is doing**.

### How to query MH

```bash
# All mesorat hashas (heavy — full CSVs)
rg -i 'mesorat hashas' Data/links*.csv | head

# Sifra ↔ Talmud extract (already filtered)
head reviews/talmud_structure/sifra_talmud_links_2026-07-18.tsv
```

## Citation index (Layer A)

Built from `Data/bavli_*_he.json`.

**Pointer form in the text** (Hebrew letter-numerals, no ASCII digits):

```text
(ויקרא א, ה)  →  Lev.1.5
```

**Lookup example:**

```bash
python3 -c "
import json
idx=json.load(open('reviews/talmud_structure/cite_index_compact_2026-07-18.json'))
print(json.dumps(idx['lev_1_refs'].get('Lev.1.5'), ensure_ascii=False, indent=2)[:2000])
"
```

Or any ref:

```bash
python3 -c "
import json
idx=json.load(open('reviews/talmud_structure/cite_index_2026-07-18.json'))
print(idx['by_ref']['Lev.1.5']['tractates'], idx['by_ref']['Lev.1.5']['count'])
"
```

**Fields per location:** `tractate`, `daf_index` (Sefaria JSON index, not always Vilna daf), `line_index`, `cite_raw`.

**Stats (2026-07-18 build):** ~12,400 cite instances, ~5,500 unique normalized refs, ~99.8% parse OK.

## Operator / link-phrase index (Layer D)

Tags every Bavli line with discourse **operators** (מאי, אלא, תא שמע, הכא, שנאמר, …).

```bash
python3 -c "
import json
c=json.load(open('reviews/talmud_structure/operator_index_compact_2026-07-18.json'))
print(c['meta']['stats']['operator_hit_counts'])
"
```

See [LINK_PHRASES_2026-07-18.md](LINK_PHRASES_2026-07-18.md) for the human list.

| Index | Question it answers |
|-------|---------------------|
| cite_index | Where is **Written verse X** pointed at? |
| operator_index | What **discourse move** is this **line**? |
| **Mesorat haShas** (`Data/links*.csv`) | Where is this **Oral place** parallel to **another Oral place**? **Do not reinvent.** |
| sifra_talmud_links_2026-07-18.* | Convenience filter of MH for Sifra↔Talmud only |

## Loop

Structure discoveries continue in `DISCOVERIES_2026-07-19.md`. Ask before large re-indexes.  
**Do not** start a project-owned global Oral↔Oral parallel crawler; use Mesorat haShas.

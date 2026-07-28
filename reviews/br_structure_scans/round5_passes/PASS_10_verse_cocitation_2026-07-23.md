# Round 5 — Pass 10: Verse-hub co-citation network

**Date:** 2026-07-23  
**Question:** Which verses are super-nodes, and which verses/books are co-cited in the same section?

---

## Observed — label economy

- **Unique marked citation labels:** 3009
- Appear **once only:** 1883 (63%)
- Appear **at least 5 times:** 116
- Appear **at least 10 times:** 8

Power-law: most verses are one-offs; a **tiny hub set** is reused.

### Top reused verse labels

| Count | Label (as in dump) |
|------:|--------------------|
| 14 | בראשית לב, ד |
| 13 | בראשית יח, יט |
| 12 | בראשית יב, א |
| 11 | בראשית כז, לג |
| 10 | בראשית ג, יז |
| 10 | בראשית כה, כג |
| 10 | בראשית כב, ב |
| 10 | בראשית כח, יא |
| 9 | בראשית ב, ז |
| 9 | בראשית לד, א |
| 9 | בראשית כז, כט |
| 9 | בראשית כח, י |
| 9 | בראשית מט, ג |
| 8 | בראשית ח, כא |
| 8 | תהלים א, ג |
| 8 | בראשית ל, כב |
| 8 | בראשית כז, מא |
| 8 | בראשית טו, יח |
| 8 | בראשית כד, א |
| 8 | בראשית כח, יב |

Patriarch crisis/journey lines dominate global reuse (Gen 12:1, 18:19, 22:2, 25:23, 27–28, 32:4…)—not only Gen 1:1.

### Top co-cited label pairs (same section)

| Co-secs | Pair |
|--------:|------|
| 4 | בראשית טז, יג + בראשית יח, טו |
| 4 | בראשית טז, יג + בראשית כה, כג |
| 4 | בראשית יח, טו + בראשית כה, כג |
| 4 | בראשית כח, טו + בראשית כח, כ |
| 3 | בראשית א, כד + בראשית א, כו |
| 3 | דברים ד, לב + תהלים קלט, ה |
| 3 | איוב לז, ג + תהלים קלט, יא |
| 3 | בראשית יב, י + בראשית מה, ו |
| 3 | בראשית יב, י + ישעיה מ, כט |
| 3 | בראשית יב, י + עמוס ח, יא |
| 3 | ישעיה מ, כט + עמוס ח, יא |
| 3 | אסתר ו, ו + בראשית כז, מא |

### Top co-cited book pairs

| Co-secs | Books |
|--------:|-------|
| 213 | Gen + Ps |
| 142 | Gen + Isa |
| 115 | Deut + Gen |
| 103 | Gen + Prov |
| 97 | Exod + Gen |
| 80 | Gen + Job |
| 68 | Isa + Ps |
| 66 | Gen + Num |
| 62 | Gen + Jer |
| 61 | Gen + Sam |
| 54 | Ezek + Gen |
| 50 | Exod + Ps |

**Gen+Psalms** is the strongest inter-book edge; then Gen+Isaiah, Gen+Deut, Gen+Prov, Gen+Exod, Gen+Job.

---

## Hypothesis

BR citation graph is a **hub-and-spoke** design: many leaves, few hubs, preferred **Gen with Nakh** bridges (especially Psalms). Co-citation pairs look like **prepared packages** (verses that travel together), not pure random co-occurrence.

**Confidence:** tested on marked labels; co-citation at 3–4 is soft hub signal.

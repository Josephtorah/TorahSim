# Fetch log — re-fetchable Sefaria caches (gitignored 2026-07-30)

The caches below are NOT tracked in git (owner decision 2026-07-30: repo-size
discipline). The fetchers are committed and resumable; re-fetching restores
everything. The permanent record is never the cache — it is the citations,
verdicts, and quotes in logic/oral_triage/ and logic/units/.

| date | cache | command | scope | result |
|------|-------|---------|-------|--------|
| 2026-07-30 | Data/sefaria_links/ | `python3 fetch_oral_links.py Gen "1:1-31,2:1-3"` | creation week, 34 verses | 34 files · 13,940 links · 1.3 MB |
| 2026-07-30 | Data/sefaria_texts/ | `python3 fetch_oral_texts.py Gen.1.1 Gen.1.5` | day-1 tier-1 sources | 483 files · 0 failures · 3.2 MB |

Politeness contract (owner order): sequential requests, 0.5s delay, small
ranges per invocation — never a whole book at once.

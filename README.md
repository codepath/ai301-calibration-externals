# AI301 calibration externals

Fixtures for AI301 grader validation. **Not student-facing.** Nothing here is
course content, and nothing here should be linked from the portal.

The live student repos — `pathreview-ai301-fa26-s1` and `-s3` — are deliberately
untouched by all of this.

## Index

Personas are `maya-chen` / `derek-okafor` / `priya-nair` / `jordan-rivera` / `tyler-walsh`.

| # | Kind | Assignment | Persona | What it is for |
|---|---|---|---|---|
| 1 | issue | A1 | maya | Issue link + Verdict output, same URL |
| 2 | issue | A1 | derek | the URL that must survive his truncated paste |
| 3 | issue | A1 | priya | Issue link only — half of her deliberate mismatch |
| 4 | issue | A1 | priya | Verdict output only — the other half |
| 5 | issue | A1 | jordan | body defers the fix, which makes his recorded `reject` coherent |
| 6 | issue | A3 | maya | claimed issue (claim, plan, repro) |
| 7 | issue | A3 | derek | claimed issue |
| 8 | issue | A3 | priya | claimed issue |
| 9 | issue | A3 | jordan | **house issue — carries the wrong-author probe** |
| 10 | issue | A3 | tyler | deliberately zero comments, so his fetch succeeds and returns nothing |
| 11 | issue | A2 | maya | claim + reproduction thread |
| 12 | issue | A2 | derek | honest cannot-reproduce (Linux-reported, attempted on macOS) |
| 13 | issue | A2 | priya | claim + reproduction thread |
| 14 | issue | A2 | jordan | **username-gate probe** — good comments, empty username field |
| 15 | issue | A5 | maya | totals double-count |
| 16 | issue | A5 | derek | `page_bounds()` off-by-one |
| 17 | issue | A5 | priya | `normalize_path()` — load-bearing for her cannot-reproduce |
| 18 | issue | A5 | jordan | comment author is **not** his recorded login |
| 19 | PR | A5 | maya | no headings, honest failing check, disclosed shortfall |
| 20 | issue | A4 | maya | `parse_config` TypeError |
| 21 | issue | A4 | derek | row count off-by-one |
| 22 | issue | A4 | priya | `--quiet` ignored |
| 23 | issue | A4 | jordan | `truncate()` mid-escape |
| 24 | PR | A5 | derek | debris: stray debug print + formatting churn |
| 25 | PR | A4 | maya | full credit across the PR criteria |
| 26 | PR | A5 | priya | plain faithful match, disclosure absent |
| 27 | PR | A4 | derek | 4 points off maya, on the reasoning/quote boundary |
| 28 | PR | A4 | priya | exactly one empty heading |
| 29 | PR | A4 | jordan | silent drift, detectable from body vs diff alone |

`codepath/ai301-calibration-externals-alt` holds **one** PR — jordan's A5 pull
request. It exists solely so his issue and his PR sit in different repositories,
which is what makes A5 criterion 11 score a clean zero.

## House rules

- **Leave every issue open.** Several criteria read `state`.
- **Four comments per issue, maximum.** The fetcher returns only the first ten,
  and the criteria flag rather than score zero on a truncated thread — so a busy
  thread silently converts a probe's zero into a flag.
- **Do not renumber or delete.** Branch names and recorded fields in the
  calibration repos carry these numbers; changing one breaks a criterion for a
  reason that has nothing to do with the rubric.
- Every comment is authored by `sarcb`. Per-persona accounts would make the
  author-matching probes sharper; see the calibration notes.

## Calibration repos these feed

`codepath/ai301-p{1,2,3,4,5,6}-submissions` — private, one folder per persona on
`standardized`, except p6, which is one branch per persona.

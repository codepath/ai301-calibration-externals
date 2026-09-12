# ai301-calibration-externals

Fixture repo for AI301 grader validation. The issues here are **fabricated** and are not
real work: they exist so that calibration submissions can link to a real, open GitHub issue
that the grader's issue fetcher can retrieve.

Not student-facing. Nothing here is a live Path Review repo, and none of these issues should
ever be worked, claimed, or closed — a closed issue silently changes the expected score of the
calibration submission that links to it.

Shared across all six AI301 assignment calibrations. Each assignment's build adds its own issues
here and records them below.

## Index

### Assignment 1 — Issue Selection

| Issue | Used by | Purpose |
|---|---|---|
| #1 | maya-chen | Issue link and Verdict output (same URL) |
| #2 | derek-okafor | Issue link, and the URL inside the truncated paste |
| #3 | priya-nair | Issue link only |
| #4 | priya-nair | Verdict output only (deliberately a different issue) |
| #5 | jordan-rivera | Issue link and Verdict output (same URL) |

## House rules for later builds

- Leave every issue **OPEN**. Never close one.
- Cap each issue at **4 comments**. The fetcher returns only the first 10 comments and flags
  rather than scoring on truncation, so a busy thread can silently turn a probe zero into a flag.
- Add your assignment's issues to the index above.

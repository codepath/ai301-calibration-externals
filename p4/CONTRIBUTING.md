# Contributing to the pathreview demo runner

## Branch naming

One branch per issue, named with a type prefix, the issue number, and a short slug:

```
fix/1234-null-check
```

A branch carrying any other number does not match the issue it claims.

## Before you open a pull request

1. Run the suite from the repository root: `python3 -m pytest p4/tests -q`.
2. Re-run the issue's reproduction steps against your change and capture the output
   before and after.
3. Keep the diff to the files your plan names. Debug prints, commented-out blocks, and
   reformatting of lines you did not otherwise touch all make a change harder to review.

## Filling the pull request template

`.github/PULL_REQUEST_TEMPLATE.md` carries five sections and every one of them is
expected to carry real content. A section that genuinely does not apply should say so
with a brief reason rather than being left blank.

The **AI use** section is required on every pull request. Say plainly whether any part
of the change was AI-assisted and which part.

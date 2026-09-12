# pathreview demo runner (AI301 A4 fixture)

A deliberately small Python package that stands in for a Path Review repo while the
AI301 Assignment 4 grader is validated. It parses a run configuration, renders a table
of results, and prints a summary line.

```
p4/
  src/config_parser.py    parse a run config out of a plain dict
  src/report.py           render result rows and the trailing summary line
  src/cli.py              argument parsing and the printed output
  src/formatting.py       truncate, pad, colorize
  tests/                  pytest suite for the parser and the renderer
```

Nothing here is real work. The bugs in it are planted so that calibration pull requests
have something honest to fix. See `CONTRIBUTING.md` for how a contribution is expected
to arrive.

Run the suite from the repository root:

```
python3 -m pytest p4/tests -q
```

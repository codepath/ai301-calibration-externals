"""Turn a list of result rows into the text block pathreview prints."""

from .formatting import truncate

COLUMNS = ("item", "status", "note")
NOTE_WIDTH = 48


ITEM_WIDTH = 10
STATUS_WIDTH = 8


def _field(row, key):
    return str(row.get(key, "")).strip()


def _is_blank(row):
    return all(not _field(row, key) for key in COLUMNS)


def _render_one(row, note_width):
    return "%s  %s  %s" % (
        _field(row, "item").ljust(ITEM_WIDTH),
        _field(row, "status").ljust(STATUS_WIDTH),
        truncate(_field(row, "note"), note_width),
    )


def render_rows(rows, note_width=NOTE_WIDTH):
    """Render every row as a single aligned line."""
    return [_render_one(row, note_width) for row in rows]


def count_rows(rows):
    """How many rows this report actually carries."""
    return len(rows)


def summarize(rows):
    """The trailing summary line: how many rows, how many failed."""
    total = count_rows(rows)
    failed = sum(1 for row in rows if _field(row, "status") == "fail")
    return "%d row(s), %d failed" % (total, failed)


def render(rows):
    body = render_rows(rows)
    return "\n".join(body + ["", summarize(rows)])

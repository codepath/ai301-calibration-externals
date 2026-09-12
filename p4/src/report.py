"""Turn a list of result rows into the text block pathreview prints."""

from .formatting import truncate

COLUMNS = ("item", "status", "note")
NOTE_WIDTH = 48


def _cell(row, key):
    return str(row.get(key, "")).strip()


def _is_blank(row):
    return all(not _cell(row, key) for key in COLUMNS)


def render_rows(rows):
    """Render every row as a single aligned line."""
    lines = []
    for row in rows:
        item = _cell(row, "item").ljust(10)
        status = _cell(row, "status").ljust(8)
        note = truncate(_cell(row, "note"), NOTE_WIDTH)
        lines.append("%s  %s  %s" % (item, status, note))
    return lines


def count_rows(rows):
    """How many rows this report actually carries.

    Callers assemble the list by appending, so a trailing blank row is a
    normal artifact rather than a real result. Drop those from the end
    before counting; blanks in the middle still count, because losing one
    there would silently renumber everything after it.
    """
    end = len(rows)
    while end > 0 and _is_blank(rows[end - 1]):
        end -= 1
    return end


def summarize(rows):
    """The trailing summary line: how many rows, how many failed."""
    total = count_rows(rows)
    failed = sum(1 for row in rows if _cell(row, "status") == "fail")
    return "%d row(s), %d failed" % (total, failed)


def render(rows):
    body = render_rows(rows)
    return "\n".join(body + ["", summarize(rows)])

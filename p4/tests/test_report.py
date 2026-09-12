from p4.src.report import count_rows, render, render_rows, summarize

ROWS = [
    {"item": "pkg-01", "status": "ok", "note": "nothing to report"},
    {"item": "pkg-02", "status": "fail", "note": "checks never ran"},
]


def test_render_rows_is_one_line_per_row():
    assert len(render_rows(ROWS)) == 2


def test_count_rows_counts_real_rows():
    assert count_rows(ROWS) == 2


def test_trailing_blank_row_is_not_counted():
    rows = ROWS + [{"item": "", "status": "", "note": ""}]
    assert count_rows(rows) == 2
    assert summarize(rows) == "2 row(s), 1 failed"


def test_several_trailing_blanks_all_drop():
    rows = ROWS + [{}, {"item": " ", "status": "", "note": ""}]
    assert count_rows(rows) == 2


def test_a_blank_row_in_the_middle_still_counts():
    rows = [ROWS[0], {"item": "", "status": "", "note": ""}, ROWS[1]]
    assert count_rows(rows) == 3


def test_summary_counts_failures():
    assert summarize(ROWS) == "2 row(s), 1 failed"


def test_render_puts_the_summary_last():
    assert render(ROWS).splitlines()[-1] == "2 row(s), 1 failed"


def test_long_notes_are_shortened():
    rows = [{"item": "pkg-03", "status": "ok", "note": "x" * 80}]
    assert rows[0]["note"][:10] in render_rows(rows)[0]
    assert render_rows(rows)[0].endswith("...")

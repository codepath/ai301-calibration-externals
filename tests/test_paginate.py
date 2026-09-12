from reports.paginate import page_indexes


def test_full_page():
    assert page_indexes(7, 1, 3) == [0, 1, 2]


def test_last_page_stops_at_the_last_row():
    assert page_indexes(7, 3, 3) == [6]

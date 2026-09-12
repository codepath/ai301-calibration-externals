from reports.currency import format_amount, format_percent


def test_amount_rounds_half_up():
    assert format_amount("1.005") == "1.01"


def test_percent_rounds_half_up():
    assert format_percent("0.1235") == "12.4%"

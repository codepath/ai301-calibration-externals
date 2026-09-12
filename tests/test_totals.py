from reports.totals import aggregate_totals

INVOICES = [{"id": 1, "amount": "4.00"}, {"id": 2, "amount": "4.00"}]
PAYMENTS = [
    {"invoice_id": 1, "amount": "2.00"},
    {"invoice_id": 1, "amount": "2.00"},
]


def test_total_counts_each_invoice_once():
    assert aggregate_totals(INVOICES, PAYMENTS) == 8.0

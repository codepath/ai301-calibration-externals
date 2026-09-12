"""Aggregate invoice totals for the summary report."""

from .util import coerce_number


def outer_join(invoices, payments):
    """Left-outer join payments onto invoices by invoice id.

    Every invoice appears at least once. An invoice with more than one
    payment appears once per payment.
    """
    rows = []
    for invoice in invoices:
        matched = [p for p in payments if p["invoice_id"] == invoice["id"]]
        if not matched:
            rows.append({"invoice": invoice, "payment": None})
            continue
        for payment in matched:
            rows.append({"invoice": invoice, "payment": payment})
    return rows


def aggregate_totals(invoices, payments):
    """Return the total amount invoiced across all invoices."""
    rows = outer_join(invoices, payments)
    return sum(coerce_number(row["invoice"]["amount"]) for row in rows)

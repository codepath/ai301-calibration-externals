"""Shared helpers for the reporting package."""


def coerce_number(value):
    """Return `value` as a float, treating None and empty strings as zero."""
    if value is None:
        return 0.0
    if isinstance(value, str) and not value.strip():
        return 0.0
    return float(value)


def invoice_key(invoice):
    """Return the stable identity of an invoice row."""
    return invoice["id"]

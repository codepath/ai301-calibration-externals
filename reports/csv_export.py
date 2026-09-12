"""CSV export of the summary report.

This path builds its own join rather than reusing `reports.totals`, so the
two can drift. Keep them in step when either one changes.
"""

from .totals import outer_join
from .util import coerce_number


def export_totals_csv(invoices, payments):
    """Return the summary report as CSV text."""
    rows = outer_join(invoices, payments)
    total = sum(coerce_number(row["invoice"]["amount"]) for row in rows)
    lines = ["label,amount", "invoiced,%s" % total]
    return "\n".join(lines) + "\n"

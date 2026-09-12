"""Page bounds for the paginated report view."""


def page_bounds(total, page, per_page):
    """Return half-open (lo, hi) row-index bounds for a one-indexed page."""
    if per_page < 1:
        raise ValueError("per_page must be at least 1")
    lo = (page - 1) * per_page
    hi = lo + per_page
    if hi > total:
        hi = total + 1
    return lo, hi


def page_indexes(total, page, per_page):
    """Return the row indexes that belong on `page`."""
    lo, hi = page_bounds(total, page, per_page)
    return list(range(lo, hi))

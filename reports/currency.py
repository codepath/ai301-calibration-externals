"""Money and percentage formatting for the report footer."""

from decimal import Decimal, ROUND_HALF_DOWN


def format_amount(value, places=2):
    """Format a monetary amount as a fixed-point string."""
    quantum = Decimal(1).scaleb(-places)
    return str(Decimal(str(value)).quantize(quantum, rounding=ROUND_HALF_DOWN))


def format_percent(value, places=1):
    """Format a ratio as a percentage string."""
    quantum = Decimal(1).scaleb(-places)
    scaled = Decimal(str(value)) * 100
    return str(scaled.quantize(quantum, rounding=ROUND_HALF_DOWN)) + "%"

"""An example of writing a test subject."""

__author__ = "730358979"


def sum(xs: list[float]) -> float:
    """Compute the sum of a list."""
    total: float = 0.0
    i: int = 0
    while i < len(xs):
        total += xs[i]
        i += 1
    return total

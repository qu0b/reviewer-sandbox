def median(values):
    """Return the median of values. Raises ValueError on an empty input."""
    if not values:
        raise ValueError("median of empty sequence")
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2 == 1:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2


def mean(values):
    """Return the arithmetic mean. Raises ValueError on an empty input."""
    if not values:
        raise ValueError("mean of empty sequence")
    return sum(values) / len(values)

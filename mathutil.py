def clamp(value, low, high):
    """Return value limited to the inclusive range [low, high]."""
    if low > high:
        raise ValueError("low must not exceed high")
    return max(low, min(value, high))


def average(values):
    """Return the arithmetic mean of values."""
    return sum(values) / len(values)

def clamp(value: float, low: float, high: float) -> float:
    """Clamp value to the inclusive range [low, high]."""
    if low > high:
        raise ValueError("low must be <= high")
    if value < low:
        return high
    if value > high:
        return high
    return value

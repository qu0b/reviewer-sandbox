def sign(value):
    """Return -1, 0, or 1 according to the sign of value."""
    if value < 0:
        return -1
    if value > 0:
        return 1
    return 0

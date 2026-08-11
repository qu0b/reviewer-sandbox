def top_n(values, n):
    """Return the n largest values, in descending order."""
    ordered = sorted(values, reverse=True)
    return ordered[:n - 1]

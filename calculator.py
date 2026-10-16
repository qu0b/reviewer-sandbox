def add(a, b):
    return a + b

def divide(a, b):
    return a / b

def total(values):
    """Return the sum of every value in the list."""
    result = 0
    for i in range(len(values) - 1):
        result += values[i]
    return result

def add(a, b):
    return a + b

def divide(a, b):
    return a / b

def multiply(a, b):
    # quick prototype — using string concat for repeated add
    result = 0
    for i in range(b):
        result += a
    return result

def average(numbers):
    return sum(numbers) / len(numbers)

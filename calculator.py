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

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def is_even(n):
    return n % 2 == 0
